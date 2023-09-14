"""
URL configuration for Galglide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from gal import views
# from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('userhome/', views.upload_image, name='userhome'),
    path('logout/', views.logoutpage, name='logout'),
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
    path('user/<int:user_id>/', views.view_user_images, name='view_user_images'),
    path('preview/<int:image_id>/', views.preview_image, name='preview_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('download/<int:image_id>/', views.download_image, name='download_image'),
    path('preview_imageip/<int:image_id>/',
         views.preview_imageip, name='preview_imageip'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
