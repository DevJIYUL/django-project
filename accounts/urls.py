from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('login/',views.login, name = 'login'),
    path('edit/',views.profile_edit, name='profile_edit'),
]