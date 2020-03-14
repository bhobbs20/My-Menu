from django.contrib import admin    
from django.urls import include,path
from django.contrib.auth import views as authentication_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', include('foods.urls')),
    path('register/',user_views.register,name='register'),
]
