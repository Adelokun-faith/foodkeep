from django.contrib import admin
from django.urls import path
from loth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('', views.menu, name="menu"),
    path('', views.about, name="about")
]
