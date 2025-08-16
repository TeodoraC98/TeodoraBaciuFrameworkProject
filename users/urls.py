from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from . import views
from trails.views import TrailListView
from django.conf import settings          
from django.conf.urls.static import static
urlpatterns = [
  
    path("register/",views.register, name = 'register'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.update_profile, name='update_profile'),
    path('profile/<str:username>/',views.profile_user, name='profile_user'),
    path('login/',
          auth_views.LoginView.as_view(
              template_name='users/login.html'), name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html',
          html_email_template_name='users/emails/password_reset_email.html'),
            name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'),
         name='logout'),
]
