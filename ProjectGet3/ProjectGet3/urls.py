from django.contrib import admin
from django.urls import path
from App3 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('loadPage/', views.loadPage),
    path('viewData/', views.viewData),
   
]
