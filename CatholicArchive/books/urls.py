from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('catalog/page<int:page>/', views.CatalogView.as_view(), name='catalog'),
    path('donate/', views.donate, name='donate'),
]
