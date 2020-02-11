from django.urls import path

from detailview.views import PostDetailExecutiveView, PostDetailJudiciaryView, PostDetailLegislativeView, \
    PostDetailProExecutiveView, PostDetailProParliamentView, PostDetailProJudiciaryView

urlpatterns = [
    path('detail/<slug>', PostDetailExecutiveView.as_view(), name='detail'),
    path('fed_jud_detail/<slug>', PostDetailJudiciaryView.as_view(), name='fed_jud_detail'),
    path('fed_leg_detail/<slug>', PostDetailLegislativeView.as_view(), name='fed_leg_detail'),
    path('pro_ex_detail/<slug>', PostDetailProExecutiveView.as_view(), name='pro_ex_detail'),
    path('par_detail/<slug>', PostDetailProParliamentView.as_view(), name='par_detail'),
    path('pro_jud_detail/<slug>', PostDetailProJudiciaryView.as_view(), name='pro_jud_detail'),
]
