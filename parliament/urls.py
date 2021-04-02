from django.urls import path
from parliament.views import Home
from parliament.views import Deputy
from parliament.views import Proposition

app_name = 'home'
urlpatterns = [
    path('', Home.index, name='index_page'),
    path('deputies/', Deputy.deputies_list, name='deputies_list_page'),
    path('deputies/search', Deputy.deputies_search, name='deputies_search_page'),
    path('deputies/<int:pk>/', Deputy.deputy_detail,
         name='deputy_detail_page'),
    path('propositions/', Proposition.propositions_list,
         name='propositions_list_page'),
    path('propositions/<int:pk>/', Proposition.proposition_detail,
         name='proposition_detail_page'),
]
