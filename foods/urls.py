from django.urls import path
from . import views

app_name = "foods"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name="item"),
    path('add', views.create_food, name="create_food"),
    path('update/<int:id>', views.update_food, name="update_food"),
    path('delete/<int:id>', views.delete_food, name="delete_food")
]
