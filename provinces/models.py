from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from base.models import BaseModel
from offices.models import ProvinceJudiciaryOffice, ExecutiveOffice, ProvincialParliamentOffice


class ProvincesName(models.Model):
    Name_of_Province = models.CharField(max_length=70)

    def __str__(self):
        return self.Name_of_Province


class ProvinceJudiciary(BaseModel):
    court = models.ForeignKey(ProvinceJudiciaryOffice, on_delete=models.DO_NOTHING, null=True, default=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pro_jud_last_modified_by',
                                         null=True,
                                         blank=True)
    select_province = models.ForeignKey(ProvincesName, on_delete=models.DO_NOTHING, null=True, default=True)

    def __str__(self):
        return self.title


class ProvinceExecutive(BaseModel):
    related_ministry = models.ForeignKey(ExecutiveOffice, on_delete=models.DO_NOTHING, null=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pro_ex_last_modified_by',
                                         null=True,
                                         blank=True)
    select_province = models.ForeignKey(ProvincesName, on_delete=models.DO_NOTHING, null=True, default=True)

    def __str__(self):
        return self.title


class ProvincialParliament(BaseModel):
    related_parliament = models.ForeignKey(ProvincialParliamentOffice, on_delete=models.DO_NOTHING, null=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pro_par_last_modified_by',
                                         null=True,
                                         blank=True)
    select_province = models.ForeignKey(ProvincesName, on_delete=models.DO_NOTHING, null=True, default=True)

    def __str__(self):
        return self.title
