from django.contrib import admin
from .models import *


class SubstcriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_filter = ['name']
    search_fields = ['name', 'email']
    fields = ['email']

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubstcriberAdmin)