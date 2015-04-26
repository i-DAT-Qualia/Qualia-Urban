from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include('config.api_urls')),

    # accounts
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^forgot/', 'accounts.views.reset_password_page'),

    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + settings.FAVICON)),
]
