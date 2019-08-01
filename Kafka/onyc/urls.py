from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from users import views as user_views


extra_patterns = [
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
# -----------password recovery patterns--------------------------


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include('books.urls'))
    path('profile/<str:username>/', user_views.ProfileView.as_view(), name='blog-profile'),
    path('profile/update', user_views.ProfileUpdate.as_view(), name='blog-profile-edit'),


    path('register/', user_views.Register.as_view(), name='users-register' ),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', login_required(auth_views.LogoutView.as_view(template_name='users/logout.html')), name='users-logout'),

    path('password_reset/', include(extra_patterns)),


    path('', include('blog.urls')),
    path('books/', include('books.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


