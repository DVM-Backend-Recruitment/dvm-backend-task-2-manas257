from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('signup/', views.signup, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('profile/',views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)