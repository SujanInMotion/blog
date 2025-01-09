"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, logoutView, user_login, signup, profile,  create_blog, edit_blog, delete,modify


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('logout/', logoutView , name = "logout"),
    path('modify/', modify , name = "modify"),
    path('login/', user_login , name = "login"),
    path('signup/', signup , name = "signup"),
    path('profile',profile,name='profile'),
    path('create-blog/', create_blog , name = "create"),
    path('edit-blog/<int:pk>/', edit_blog , name = 'edit-blog'),
    path('delete/<int:pk>', delete , name = "delete")    
]
