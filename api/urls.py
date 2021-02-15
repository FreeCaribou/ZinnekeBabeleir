from django.urls import path

from api.services import DeputyService
from api.services import VoteService
from api.services import LegislatureService
from api.services import PartyService
from api.services import PropositionService

app_name = 'api'
urlpatterns = [
    # path('error/<string:message>', views.error, name='error'),
    path('deputies/', DeputyService.deputies, name='deputies'),
    path('deputies/<int:deputy_id>', DeputyService.deputy, name='deputy'),
    path('votes/', VoteService.votes, name='votes'),
    path('legislatures/', LegislatureService.legislatures, name='legislatures'),
    path('parties/', PartyService.parties, name='parties'),
    path('parties/<int:party_id>', PartyService.party, name='party'),
    path('propositions/', PropositionService.propositions, name='propositions'),
    path('propositions/<int:proposition_id>',
         PropositionService.proposition, name='proposition')
]
