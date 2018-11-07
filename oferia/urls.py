from django.urls import path
from . import views


urlpatterns = [
    path('', views.oferia_list, name='oferia_list'),
    path('offer/<int:pk>/', views.offer_detail, name='offer_detail'),
    path('offer/new', views.offer_new_edit, name='offer_new_edit')
]
