from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, UpdateView, DeleteView

from provinces.forms import ProExecutiveForm, ProJudiciaryForm, ProParliamentForm
from provinces.models import ProvinceExecutive, ProvinceJudiciary, ProvincialParliament


class ProExecutiveListView(ListView):
    model = ProvinceExecutive
    template_name = 'cdb/provinces/executive/executive_data_list.html'
    context_object_name = 'executive_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def pro_upload(request):
    upload = ProExecutiveForm()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            upload = ProExecutiveForm(request.POST, request.FILES)
            if upload.is_valid():
                form = upload.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('pro-add-executive')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('pro-add-executive')

        else:
            return render(request, 'cdb/provinces/executive/add_executive_data.html', {'upload_pro': upload})
    else:
        return redirect('entry-login')


class ProExecutiveUpdateView(UpdateView):
    model = ProvinceExecutive
    template_name = 'cdb/provinces/executive/executive_update.html'
    context_object_name = 'executive_table'
    fields = (
        'title', 'slug', 'content', 'category', 'related_file', 'description', 'is_private', 'is_published', 'related_ministry')

    def get_success_url(self):
        return reverse_lazy('pro-executive-data')


class ProExecutiveDelete(DeleteView):
    model = ProvinceExecutive
    template_name = 'cdb/partials/_pro-delete.html'
    context_object_name = 'executive_table'

    def get_success_url(self):
        return reverse_lazy('pro-executive-data')


# Provincial Judiciary Views
class ProvincialJudiciaryListView(ListView):
    model = ProvinceJudiciary
    template_name = 'cdb/provinces/judiciary/judiciary_table_list.html'
    context_object_name = 'pro_judiciary_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def pro_judiciary_upload(request):
    pro_add_jud = ProJudiciaryForm()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            pro_add_jud = ProJudiciaryForm(request.POST, request.FILES)
            if pro_add_jud.is_valid():
                form = pro_add_jud.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('pro-add-judiciary')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('pro-add-judiciary')

        else:
            return render(request, 'cdb/provinces/judiciary/judiciary_add_data.html', {'pro_add_jud': pro_add_jud})
    else:
        return redirect('entry-login')


class ProvincialJudiciaryUpdateView(UpdateView):
    model = ProvinceJudiciary
    template_name = 'cdb/provinces/judiciary/judiciary_update.html'
    context_object_name = 'pro_judiciary_table'
    fields = ('title', 'slug', 'content', 'category', 'related_file', 'description', 'is_private', 'is_published', 'court')

    def get_success_url(self):
        return reverse_lazy('pro-judiciary-data')


class ProvincialJudiciaryDelete(DeleteView):
    model = ProvinceJudiciary
    template_name = 'cdb/provinces/judiciary/_delete.html'
    context_object_name = 'pro_judiciary_table'

    def get_success_url(self):
        return reverse_lazy('pro-judiciary-data')


# Provincial Parliament Views
class ProvincialParliamentListView(ListView):
    model = ProvincialParliament
    template_name = 'cdb/provinces/parliament/parliament_table_list.html'
    context_object_name = 'pro_parliament_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def parliament_upload(request):
    pro_add_par = ProParliamentForm()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            pro_add_par = ProParliamentForm(request.POST, request.FILES)
            if pro_add_par.is_valid():
                form = pro_add_par.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('pro-add-parliament')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('pro-add-parliament')

        else:
            return render(request, 'cdb/provinces/parliament/parliament_add_data.html', {'pro_add_par': pro_add_par})
    else:
        return redirect('entry-login')


class ProvincialParliamentUpdateView(UpdateView):
    model = ProvincialParliament
    template_name = 'cdb/provinces/parliament/parliament_update.html'
    context_object_name = 'pro_parliament_table'
    fields = (
        'title', 'slug', 'content', 'category', 'related_file', 'description', 'is_private', 'is_published',
        'related_parliament')

    def get_success_url(self):
        return reverse_lazy('pro-parliament-data')


class ProvincialParliamentDelete(DeleteView):
    model = ProvincialParliament
    template_name = 'cdb/provinces/parliament/_delete.html'
    context_object_name = 'pro_parliament_table'

    def get_success_url(self):
        return reverse_lazy('pro-parliament-data')
