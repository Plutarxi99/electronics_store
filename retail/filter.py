import django_filters

from retail.models import UnionChain


class UnionChainCountryFilter(django_filters.rest_framework.FilterSet):
    """
    Для более удобного написания фильтра при запросе
    """
    country = django_filters.CharFilter(field_name='contact__country')

    class Meta:
        model = UnionChain
        fields = ('country', )