from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from api.models import CustomUser

# Register your models here.

admin.site.register(CustomUser, SimpleHistoryAdmin)
