from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings

import dashboard.views
import accounts.views
import trees.views
import config.api_urls
import registration.backends.default.urls
import dashboard.urls

urlpatterns = [
    url(r'^$', dashboard.views.front_page),
    url(r'^trees/json/(?P<id>[^/]+)/', trees.views.return_tree_json),
    url(r'^trees/geojson/', trees.views.return_geojson),
    url(r'^trees/', dashboard.views.tree_map),
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
