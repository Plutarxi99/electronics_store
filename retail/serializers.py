from rest_framework import serializers, relations
from rest_framework.fields import SerializerMethodField

from retail.models import UnionChain, Product, Contact
from retail.validators import LevelSupplierValidator


class ContactListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображение ввиде списка контакты звена сети
    """
    class Meta:
        model = Contact
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображение ввиде списка продукт звена сети
    """
    class Meta:
        model = Product
        fields = '__all__'


class UnionChainSerializer(serializers.ModelSerializer):
    product = SerializerMethodField()
    supplier = relations.SlugRelatedField(slug_field='name', queryset=UnionChain.objects.all())
    contact = SerializerMethodField()

    def get_contact(self, contact):
        # отображение ввиде списка контакты звена сети
        return ContactListSerializer(Contact.objects.filter(contact=contact), many=True).data

    def get_product(self, product):
        # отображение ввиде списка продукта звена сети
        return ProductListSerializer(Product.objects.filter(product=product), many=True).data

    class Meta:
        model = UnionChain
        fields = "__all__"
        read_only_fields = ['debt', ]


class UnionChainSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = UnionChain
        fields = "__all__"
        read_only_fields = ['debt', ]
        validators = [LevelSupplierValidator(obj='self')]


class UnionChainSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = UnionChain
        fields = "__all__"
        read_only_fields = ['debt', ]
        validators = [LevelSupplierValidator(obj='self')]
