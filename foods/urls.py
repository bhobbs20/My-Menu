from django.urls import path
from . import views

app_name = "foods"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name="item"),
]
