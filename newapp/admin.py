from django.contrib import admin
from .models import Company, ActivityTheme

@admin.register(ActivityTheme)
class ActivityThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'region', 'priority', 'display_activities')
    list_filter = ('priority', 'activity_themes')
    search_fields = ('name', 'short_name', 'region')
    filter_horizontal = ('activity_themes',)
    list_per_page = 20
    
    def display_activities(self, obj):
        return ", ".join([activity.name for activity in obj.activity_themes.all()])
    display_activities.short_description = 'Виды деятельности'