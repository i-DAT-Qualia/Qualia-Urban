from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from qualia.accounts.models import *


admin.site.register(QualiaUser)
