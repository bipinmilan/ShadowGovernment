from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView

from Federal.models import Executive, Judiciary, Legislative
from provinces.models import ProvinceExecutive, ProvincialParliament, ProvinceJudiciary


class PostDetailExecutiveView(DetailView):
    model = Executive
    template_name = 'Detail/detail_view.html'
    context_object_name = 'detail'


class PostDetailJudiciaryView(DetailView):
    model = Judiciary
    template_name = 'Detail/detail_view.html'
    context_object_name = 'detail'


class PostDetailLegislativeView(DetailView):
    model = Legislative
    template_name = 'Detail/detail_view.html'
    context_object_name = 'detail'


class PostDetailProExecutiveView(DetailView):
    model = ProvinceExecutive
    template_name = 'Detail/detail_view.html'
    context_object_name = 'detail'


class PostDetailProParliamentView(DetailView):
    model = ProvincialParliament
    template_name = 'Detail/detail_view.html'
    context_object_name = 'detail'


class PostDetailProJudiciaryView(DetailView):
    model = ProvinceJudiciary
    template_name = 'Detail/detail_view.html'
    context_object_name = 'detail'
