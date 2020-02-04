from django.shortcuts import render

# Create your views
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from Federal.models import Executive, Legislative, Judiciary
from django.db.models import Q
from django.views.generic import ListView

from provinces.models import ProvinceExecutive, ProvincialParliament, ProvinceJudiciary

'''class HomeView(TemplateView):
    template_name = 'search_page/search_result.html'''


class HomeView(TemplateView):
    template_name = 'search_page/home.html'


'''class FederalListView(ListView):
    template_name = 'search_page/search_result.html'
    model = Executive
    queryset = Executive.objects.all()
    context_object_name = 'executive'''


def search(request):
    fed_executive_queryset_list = Executive.objects.order_by('-title')
    fed_legislative_queryset_list = Legislative.objects.order_by('-title')
    fed_judiciary_queryset_list = Judiciary.objects.order_by('-title')

    # provincial queryset list
    pro_executive_queryset_list = ProvinceExecutive.objects.order_by('-title')
    pro_parliament_queryset_list = ProvincialParliament.objects.order_by('-title')
    pro_judiciary_queryset_list = ProvinceJudiciary.objects.order_by('-title')

    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            federal_executive_results = fed_executive_queryset_list.filter(Q(title__icontains=q) |
                                                                           Q(
                                                                               related_ministry__name__icontains=q)).distinct()

            federal_judiciary_results = fed_judiciary_queryset_list.filter(Q(title__icontains=q) |
                                                                           Q(
                                                                               related_court__name__icontains=q)).distinct()

            federal_legislative_results = fed_legislative_queryset_list.filter(Q(title__icontains=q) |
                                                                               Q(
                                                                                   related_house__name__icontains=q)).distinct()

            # provincial results
            pro_executive_results = pro_executive_queryset_list.filter(Q(title__icontains=q) |
                                                                       Q(
                                                                           related_ministry__name__icontains=q) | Q(
                select_province__Name_of_Province__icontains=q)).distinct()

            pro_judiciary_results = pro_judiciary_queryset_list.filter(Q(title__icontains=q) |
                                                                       Q(
                                                                           court__name__icontains=q) | Q(
                select_province__Name_of_Province__icontains=q)).distinct()

            pro_parliament_results = pro_parliament_queryset_list.filter(Q(title__icontains=q) |
                                                                         Q(
                                                                             related_parliament__parliament_name__icontains=q) | Q(
                select_province__Name_of_Province__icontains=q)).distinct()

            context = {
                'fed_executive_items': federal_executive_results,
                'fed_judiciary_items': federal_judiciary_results,
                'fed_legislative_items': federal_legislative_results,
                # provincial context items
                'pro_executive_items': pro_executive_results,
                'pro_judiciary_items': pro_judiciary_results,
                'pro_parliament_items': pro_parliament_results,
            }
            return render(request, 'search_page/search_result.html', context)
