from django.contrib import admin

from repository.models import Party, Legislature, Deputy, Proposition, Vote


@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'party']


class DeputyInLine(admin.TabularInline):
    model = Deputy
    fieldsets = (
        (None, {
            'fields': ['first_name', 'last_name'],
        }),
    )
    extra = 1


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['proposition', 'deputy', 'type_code']


class VoteInline(admin.TabularInline):
    model = Vote
    fieldsets = (
        (None, {
            'fields': ['deputy', 'type_code'],
        }),
    )
    extra = 1


@admin.register(Proposition)
class PropositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'legislature']
    inlines = [VoteInline]


class PropositionInline(admin.TabularInline):
    model = Proposition
    fieldsets = (
        (None, {
            'fields': ['title', 'date', 'legislature'],
        }),
    )
    extra = 1


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    inlines = [DeputyInLine]


@admin.register(Legislature)
class LegislatureAdmin(admin.ModelAdmin):
    inlines = [PropositionInline]
