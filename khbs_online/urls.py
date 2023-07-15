from . import views
from django.urls import path

app_name = 'online'
urlpatterns = [
    path('programs', views.programs, name='programs'),
    path('add-program/<str:title>', views.add_to_user_course, name='add-course'),
    path('add-sp-program/<str:title>', views.add_to_user_special_course, name='add-sp-course'),
    path('profile/remove-program/<str:title>', views.remove_from_user_course, name='remove-course'),
    path('profile/remove-specialprogram/<str:title>', views.remove_from_user_special_course, name='remove-sp-course'),
    path('profile/<str:user>', views.profile, name='profile'),
    path('profile/course/series/<int:id>', views.course_series, name='course-series'),
    path('signup', views.signup, name='signup'),
    path('signin', views.login_view, name='signin'),
    path('logout', views.logout_view, name='logout'),
]