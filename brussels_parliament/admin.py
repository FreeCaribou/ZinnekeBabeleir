from django.contrib import admin

from repository.models import Party, Legislature, Deputy


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    pass


@admin.register(Legislature)
class LegislatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'party']
