from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin

class Reaction_Time_Admin (ExportActionMixin, admin.ModelAdmin):
    list_display = ('subject', 'signal', 'reactionTime')

class Subject_Admin (ExportActionMixin, admin.ModelAdmin):
    list_display = ('age', 'gender', 'nationality', 'driversLicense', "yearsXP")

class Signal_Admin (ExportActionMixin, admin.ModelAdmin):
    list_display = ('description', 'signalType', 'frequency', 'imgURL')

class Preference_Admin (ExportActionMixin, admin.ModelAdmin):
    list_display = ('subject', 'signal', 'preference')

class Importance_Admin (ExportActionMixin, admin.ModelAdmin):
    list_display = ('subject', 'signal', 'importance')
    
class Identify_Admin (ExportActionMixin, admin.ModelAdmin):
    list_display = ('subject', 'signal', 'guess')

# Register your models here.
admin.site.register(Subject, Subject_Admin)
admin.site.register(Signal, Signal_Admin)
admin.site.register(Reaction_Time, Reaction_Time_Admin)
admin.site.register(Preference, Preference_Admin)
admin.site.register(Importance, Importance_Admin)
admin.site.register(Identify, Identify_Admin)