from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^api/v3/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
