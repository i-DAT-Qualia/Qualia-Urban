from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings

import dashboard.views
import accounts.views
import config.api_urls
import registration.backends.default.urls
import dashboard.urls
import trees.urls
import airquality.urls

urlpatterns = [
    url(r'^$', dashboard.views.front_page),
    url(r'^trees/', include(trees.urls)),
    url(r'^aqs/', include(airquality.urls)),
    url(r'^draft/', dashboard.views.draft_page),
    url(r'^props/', dashboard.views.props_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include(config.api_urls)),

    # accounts
    url(r'^accounts/', include(registration.backends.default.urls)),
    url(r'^forgot/', accounts.views.reset_password_page),
    url(r'dashboard/', include(dashboard.urls)),

    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + settings.FAVICON)),
]
