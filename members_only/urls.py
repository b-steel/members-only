"""members_only URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as authviews

from apps.core.views import FrontPage, PostView
from apps.accounts.views import Signup, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontPage.as_view(), name='frontpage'),
    path('accounts/signup/', Signup.as_view(), name='signup'),
    path('accounts/login/', authviews.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', authviews.LogoutView.as_view(), name='logout'),
    path('create_post/', PostView.as_view(), name='create_post'),
    path('u/<str:username>/', ProfileView.as_view(), name='profile'),

]
