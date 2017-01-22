from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^$', views.home, name='home'),
] 
