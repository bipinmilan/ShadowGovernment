from django.contrib.auth.decorators import login_required

from provinces import views
from django.urls import path

from provinces.views import ProExecutiveListView, ProExecutiveUpdateView, ProExecutiveDelete, \
    ProvincialJudiciaryListView, ProvincialJudiciaryUpdateView, ProvincialJudiciaryDelete, ProvincialParliamentListView, \
    ProvincialParliamentUpdateView, ProvincialParliamentDelete

urlpatterns = [
    path('pro-add-executive', views.pro_upload, name='pro-add-executive'),
    path('pro-executive-data', login_required(login_url='entry-login')(ProExecutiveListView.as_view()),
         name='pro-executive-data'),
    path('pro-executive/<int:pk>/update', login_required(login_url='entry-login')(ProExecutiveUpdateView.as_view()),
         name='pro-executive-update'),
    path('executive/<int:pk>/delete', login_required(login_url='entry-login')(ProExecutiveDelete.as_view()),
         name='executive-delete'),

    # Judiciary CRUD
    path('pro-judiciary-data', login_required(login_url='entry-login')(ProvincialJudiciaryListView.as_view()),
         name='pro-judiciary-data'),
    path('pro-add-judiciary', views.pro_judiciary_upload, name='pro-add-judiciary'),
    path('pro-judiciary/<int:pk>/update',
         login_required(login_url='entry-login')(ProvincialJudiciaryUpdateView.as_view()),
         name='pro-judiciary-update'),
    path('pro-judiciary/<int:pk>/delete', login_required(login_url='entry-login')(ProvincialJudiciaryDelete.as_view()),
         name='pro-judiciary-delete'),

    # Parliament CRUD
    path('pro-parliament-data', login_required(login_url='entry-login')(ProvincialParliamentListView.as_view()),
         name='pro-parliament-data'),
    path('pro-add-parliament', views.parliament_upload, name='pro-add-parliament'),
    path('pro-parliament/<int:pk>/update',
         login_required(login_url='entry-login')(ProvincialParliamentUpdateView.as_view()),
         name='pro-parliament-update'),
    path('pro-parliament/<int:pk>/delete', login_required(login_url='entry-login')(ProvincialParliamentDelete.as_view()),
         name='pro-parliament-delete'),

]
