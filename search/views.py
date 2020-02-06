from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from Federal.models import Executive, Legislative, Judiciary
from django.db.models import Q
from django.views.generic import ListView

from provinces.models import ProvinceExecutive, ProvincialParliament, ProvinceJudiciary
from django.http import HttpResponse

'''class HomeView(TemplateView):
    template_name = 'search_page/search_result.html'''


class HomeView(TemplateView):
    template_name = 'search_page/home.html'


'''class FederalListView(ListView):
    template_name = 'search_page/search_result.html'
    model = Executive
    queryset = Executive.objects.all()
    context_object_name = 'executive'''


# for public:- public data where published = True

def search(request):
    fed_executive_queryset_list = Executive.objects.order_by('-title').filter(is_private=False, is_published=True)
    fed_legislative_queryset_list = Legislative.objects.order_by('-title').filter(is_private=False,
                                                                                  is_published=True)
    fed_judiciary_queryset_list = Judiciary.objects.order_by('-title').filter(is_private=False, is_published=True)

    # provincial queryset list
    pro_executive_queryset_list = ProvinceExecutive.objects.order_by('-title').filter(is_private=False,
                                                                                      is_published=True)
    pro_parliament_queryset_list = ProvincialParliament.objects.order_by('-title').filter(is_private=False,
                                                                                          is_published=True)
    pro_judiciary_queryset_list = ProvinceJudiciary.objects.order_by('-title').filter(is_private=False,
                                                                                      is_published=True)

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


def private_search(request):
    if request.user is not None and request.user.is_superuser or request.user.groups.filter(name="Federal_Executive") or request.user.groups.filter(
            name="Federal_Legislative") or request.user.groups.filter(name="Federal_Judiciary").exists():
        ad_fed_executive_queryset_list = Executive.objects.order_by('-title').filter(is_published=True)
        ad_fed_legislative_queryset_list = Legislative.objects.order_by('-title').filter(
            is_published=True)
        ad_fed_judiciary_queryset_list = Judiciary.objects.order_by('-title').filter(is_published=True)

        # provincial queryset list
        ad_pro_executive_queryset_list = ProvinceExecutive.objects.order_by('-title').filter(is_published=True)
        ad_pro_parliament_queryset_list = ProvincialParliament.objects.order_by('-title').filter(is_published=True)
        ad_pro_judiciary_queryset_list = ProvinceJudiciary.objects.order_by('-title').filter(is_published=True)

        if 'q' in request.GET:
            q = request.GET['q']
            if q:
                ad_federal_executive_results = ad_fed_executive_queryset_list.filter(Q(title__icontains=q) |
                                                                                     Q(
                                                                                         related_ministry__name__icontains=q)).distinct()

                ad_federal_judiciary_results = ad_fed_judiciary_queryset_list.filter(Q(title__icontains=q) |
                                                                                     Q(
                                                                                         related_court__name__icontains=q)).distinct()

                ad_federal_legislative_results = ad_fed_legislative_queryset_list.filter(Q(title__icontains=q) |
                                                                                         Q(
                                                                                             related_house__name__icontains=q)).distinct()

                # provincial results
                ad_pro_executive_results = ad_pro_executive_queryset_list.filter(Q(title__icontains=q) |
                                                                                 Q(
                                                                                     related_ministry__name__icontains=q) | Q(
                    select_province__Name_of_Province__icontains=q)).distinct()

                ad_pro_judiciary_results = ad_pro_judiciary_queryset_list.filter(Q(title__icontains=q) |
                                                                                 Q(
                                                                                     court__name__icontains=q) | Q(
                    select_province__Name_of_Province__icontains=q)).distinct()

                ad_pro_parliament_results = ad_pro_parliament_queryset_list.filter(Q(title__icontains=q) |
                                                                                   Q(
                                                                                       related_parliament__parliament_name__icontains=q) | Q(
                    select_province__Name_of_Province__icontains=q)).distinct()

                context = {
                    'ad_fed_executive_items': ad_federal_executive_results,
                    'ad_fed_judiciary_items': ad_federal_judiciary_results,
                    'ad_fed_legislative_items': ad_federal_legislative_results,
                    # provincial context items
                    'ad_pro_executive_items': ad_pro_executive_results,
                    'ad_pro_judiciary_items': ad_pro_judiciary_results,
                    'ad_pro_parliament_items': ad_pro_parliament_results,
                }
                return render(request, 'search_page/admin_search.html', context)
    else:
        return redirect('/admin/login')
