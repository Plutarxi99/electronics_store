from rest_framework.exceptions import ValidationError

from retail.models import UnionChain


class LevelSupplierValidator:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self, value):
        """
        Метод класс для его вызова
        Валидирует, чтобы поставщик находился ниже по уровню сети
        """
        level_union: UnionChain | int = dict(value).get("level_union")  # получение уровня звена в сети
        sup: UnionChain | int = dict(value).get("supplier")  # получение уровня звена поставщик в сети
        supplier = sup.level_union
        diff = level_union - supplier
        if diff < 0:
            raise ValidationError(f'Поставщик должен стоять ниже по иерархии сети')