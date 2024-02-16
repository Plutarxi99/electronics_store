from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from retail.models import UnionChain
from retail.serializers import UnionChainSerializer


class UnionChainCreateAPIView(generics.CreateAPIView):
    """
    Создание привычки
    """
    serializer_class = UnionChainSerializer
    permission_classes = [IsAuthenticated]


class UnionChainListAPIView(generics.ListAPIView):
    """
    Отображение списка опубликованных привычек в приложении
    """
    queryset = UnionChain.objects.all()
    serializer_class = UnionChainSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['contact__country', ]
    permission_classes = [IsAuthenticated]


class UnionChainRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отображение одной привычки
    """
    queryset = UnionChain.objects.all()
    serializer_class = UnionChainSerializer
    permission_classes = [IsAuthenticated]


class UnionChainUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление привычки
    """
    queryset = UnionChain.objects.all()
    serializer_class = UnionChainSerializer
    permission_classes = [IsAuthenticated]


class UnionChainDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление привычки
    """
    queryset = UnionChain.objects.all()
    permission_classes = [IsAuthenticated]
