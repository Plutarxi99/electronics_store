from retail.apps import RetailConfig
from django.urls import path

from retail import views

app_name = RetailConfig.name

urlpatterns = [
    path('create/', views.UnionChainCreateAPIView.as_view(), name='union_chain_create'),
    path('', views.UnionChainListAPIView.as_view(), name='union_chain_list'),
    path('<int:pk>/', views.UnionChainRetrieveAPIView.as_view(), name='union_chain_detail'),
    path('update/<int:pk>/', views.UnionChainUpdateAPIView.as_view(), name='union_chain_update'),
    path('delete/<int:pk>/', views.UnionChainDestroyAPIView.as_view(), name='union_chain_delete'),
]
