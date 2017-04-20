"""image_detection_and_recognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Image_recognition import views
from django.conf import settings
from django.conf.urls.static import static
from Image_recognition import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name = 'index'),
    url(r'^list/', views.list,name = 'list'),
    url(r'^digit_recognize/',views.digit_recognize,name = 'digit_recognize'),
    url(r'^face_recognize/',views.face_recognize,name = 'face_recognize'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
