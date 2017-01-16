from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gongzang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authapp.urls', namespace='authapp')),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^', include('main.urls', namespace='main'))
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )