from django.urls import path
from search import views
from search.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('admin-search/', views.private_search, name='admin-search'),
]
