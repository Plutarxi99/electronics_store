from django.contrib import admin
from retail.models import Contact, Product, UnionChain
from django.contrib import messages
from django.utils.translation import ngettext
from django.urls import reverse


@admin.register(UnionChain)
class UnionChainAdmin(admin.ModelAdmin):
    list_display = ["name", "contact", "supplier", "debt", "url_supplier", ]
    list_display_links = ["name", "supplier", ]
    list_filter = ["contact__city", ]
    search_fields = ['contact__city', ]
    actions = ["refresh_debt", ]
    readonly_fields = ["created_at", ]

    @admin.action(description="Обновление задолжности")
    def refresh_debt(self, request, queryset):
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

    @admin.display(description="Ссылка на поставщика")
    def url_supplier(self, uc: UnionChain):
        return f"http://localhost:8000/{uc.name}"


admin.site.register(Contact)
admin.site.register(Product)

