from django.contrib import admin

from action.models import ActionSeries, Action


class ActionAdmin(admin.ModelAdmin):
    list_display = ['video']


class ActionSeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']


admin.site.register(ActionSeries, ActionSeriesAdmin)
admin.site.register(Action, ActionAdmin)
# Register your models here.
