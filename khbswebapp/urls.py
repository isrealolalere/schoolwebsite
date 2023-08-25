# for language translation
from django.views.i18n import set_language
# or alternatively
# from django.conf.urls.i18n import set_language

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register/student-info', views.admission1_reg, name='register1'),
    path('register/parent-info/<int:st_id>', views.admission2_reg, name='register2'),
    path('newsletter', views.news_letter, name='news_letter'),

    # for language translation
    path('set-language/', set_language, name='set_language'),
    # or alternatively
    # path('i18n/', set_language, name='set_language'),
]