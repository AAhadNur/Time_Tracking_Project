
from django.urls import path
from django.contrib.auth import views as auth_views

from userprofile import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('myaccount/edit-profile/', views.edit_profile, name="edit_profile"),
]
