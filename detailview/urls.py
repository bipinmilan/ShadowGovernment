from django.urls import path

from detailview.views import PostDetailExecutiveView, PostDetailJudiciaryView, PostDetailLegislativeView

urlpatterns = [
    path('detail/<int:pk>', PostDetailExecutiveView.as_view(), name='detail'),
    path('fed_jud_detail/<int:pk>', PostDetailJudiciaryView.as_view(), name='fed_jud_detail'),
    path('fed_leg_detail/<int:pk>', PostDetailLegislativeView.as_view(), name='fed_leg_detail'),
]
