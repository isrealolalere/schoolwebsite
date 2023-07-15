from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register/student-info', views.admission1_reg, name='register1'),
    path('register/parent-info/<int:st_id>', views.admission2_reg, name='register2'),
]