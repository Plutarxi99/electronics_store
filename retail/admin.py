from django.contrib import admin
from rest_framework.reverse import reverse

from retail.models import Contact, Product, UnionChain
from django.contrib import messages
from django.utils.translation import ngettext
from django.forms import ModelForm
from django.urls import reverse
from django.utils.html import escape, mark_safe


class AnswerForm(ModelForm):
    class Meta:
        model = UnionChain
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Переопределение набора поля для показа только предыдущих по иерархии объектов сети
        # или если это Завод (0), то можно сослаться на завод
        self.fields["supplier"].queryset = UnionChain.objects.filter(
            level_union=self.instance.level_union) if (
                self.instance.level_union == UnionChain.LevelUnion.FACTORY.value or
                self.instance.level_union is None) else UnionChain.objects.filter(
            level_union=self.instance.level_union - 1)


@admin.register(UnionChain)
class UnionChainAdmin(admin.ModelAdmin):
    form = AnswerForm
    list_display = ["name", "contact", "debt", "url_supplier", ]
    list_display_links = ["name", ]
    list_filter = ["contact__city", ]
    search_fields = ['contact__city', ]
    actions = ["refresh_debt", ]
    readonly_fields = ["created_at", "level_in_retail", ]

    @admin.display(description="Ссылка на поставщика")
    def url_supplier(self, obj: UnionChain):
        """
        Добавление ссылки на поставщика
        """
        link = reverse("admin:retail_unionchain_change", args=[obj.supplier_id])
        return mark_safe(f'<a href="{link}">{escape(obj.supplier.__str__())}</a>')

    @admin.action(description="Обновление задолжности")
    def refresh_debt(self, request, queryset):
        """
        Кнопка активности для обнуление задолженности
        """
        updated = queryset.update(debt=0)
        self.message_user(
            request,
            ngettext(
                "%d обнулена задолженность",
                "%d обнулены задолженности",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.register(Contact)
admin.site.register(Product)
