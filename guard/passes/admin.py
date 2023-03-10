from django.contrib import admin

from .models import Pass, PassHolder


class PassHolderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'person', 'photo')
    search_fields = ('pk', )


admin.site.register(PassHolder, PassHolderAdmin)
admin.site.register(Pass)
