from django.contrib import admin

from repository.models import Party, Legislature, Deputy, Proposition, Vote

from django import forms


class PropositionDetailFormWidget(forms.ModelForm):
    detail = forms.Textarea()
    detail.required = False

    class Media:
        css = {'all': [
            'https://cdn.jsdelivr.net/npm/sceditor@3/minified/themes/default.min.css']}
        js = ['https://cdn.jsdelivr.net/npm/sceditor@3/minified/sceditor.min.js', 'js/admin.js']


@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'party']
    search_fields = ['first_name', 'last_name']
    list_filter = ['party']


class DeputyInLine(admin.TabularInline):
    model = Deputy
    fieldsets = (
        (None, {
            'fields': ['first_name', 'last_name'],
        }),
    )
    extra = 1


class DeputyForLegislatureInLine(admin.TabularInline):
    model = Legislature.deputies.through
    readonly_fields = ['deputy']
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False


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
    readonly_fields = ['deputy']
    extra = 1


@admin.register(Proposition)
class PropositionAdmin(admin.ModelAdmin):
    list_display = ['title_fr', 'title_nl', 'date', 'legislature']
    inlines = [VoteInline]
    search_fields = ['title_fr', 'title_nl']
    list_filter = ['date', 'legislature']

    form = PropositionDetailFormWidget


class PropositionInline(admin.TabularInline):
    model = Proposition
    fieldsets = (
        (None, {
            'fields': ['title_fr', 'title_nl', 'date', 'legislature'],
        }),
    )
    extra = 1


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    inlines = [DeputyInLine]


@admin.register(Legislature)
class LegislatureAdmin(admin.ModelAdmin):
    inlines = [DeputyForLegislatureInLine, PropositionInline]
