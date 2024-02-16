from rest_framework import serializers, relations

from retail.models import UnionChain, Product


class UnionChainSerializer(serializers.ModelSerializer):
    product = relations.SlugRelatedField(slug_field='name', queryset=Product.objects.all())
    supplier = relations.SlugRelatedField(slug_field='name', queryset=UnionChain.objects.all())

    class Meta:
        model = UnionChain
        fields = ['name', 'contact', 'product', 'supplier', 'created_at', 'debt', ]
        read_only_fields = ['debt', ]
