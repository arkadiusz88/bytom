from django.urls import path
from . import views


urlpatterns = {
    path('', views.oferia_list, name='oferia_list')
}
