"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include # path() Function Returns an element for inclusion in urlpatterns with 4 args: Two required route and view and two are optional kwargs and name path(route, view, kwargs=None, name=None).'include()' adds urls from your app directory's urls.py to the main urls.py (in memory). This keeps the main urls.py from getting too big to read.

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls), # This line means that for every URL that starts with admin/, Django will find a corresponding view.
    path('', include('blog.urls')), # import URLs from our blog application to the main mysite/urls.py file.It will import blog.urls.Django will now redirect everything that comes into 'http://127.0.0.1:8000/' to blog.urls and looks for further instructions there.
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]
