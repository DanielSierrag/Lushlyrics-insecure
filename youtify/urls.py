from django.contrib import admin
from django.urls import path, include
from youtyfy_auth.views import profile
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', profile, name='profile'),
    path('', include(tf_urls)),  # Two factor auth
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),
]
