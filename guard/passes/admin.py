from django.contrib import admin

from .models import PassHolder


class PassHolderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'person', 'photo')
    search_fields = ('pk', )


admin.site.register(PassHolder, PassHolderAdmin)
