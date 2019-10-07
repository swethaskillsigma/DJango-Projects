from django.contrib import admin
from django.urls import path
from App5 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud/',views.stud),
    path('hi/',views.hi),
]
