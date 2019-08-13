from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('our_clients.urls')),
    path('signup/', user_views.SignUp, name="sign-up"),
    path('signin/', auth_views.LoginView.as_view(template_name="users/signin.html"), name="sign-in"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="log-out"),
    path('profile/', user_views.profile, name="profile"),
]

# Setttingd the URL for our media files By First Checking The if We are in Debug Mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
