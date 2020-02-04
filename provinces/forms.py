from provinces.models import ProvinceExecutive, ProvinceJudiciary, ProvincialParliament
from django import forms


class ProExecutiveForm(forms.ModelForm):
    class Meta:
        model = ProvinceExecutive
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']


class ProJudiciaryForm(forms.ModelForm):
    class Meta:
        model = ProvinceJudiciary
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']


class ProParliamentForm(forms.ModelForm):
    class Meta:
        model = ProvincialParliament
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']
