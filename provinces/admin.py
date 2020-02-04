from django.contrib import admin

# Register your models here.
from provinces.models import ProvinceJudiciary, ProvinceExecutive, ProvincialParliament, ProvincesName


class ProvinceExecutiveAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'select_province', 'related_ministry', 'category', 'is_private',
        'last_modified_by', 'timestamp', 'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = (
    'title', 'description', 'author__username', 'related_ministry__name', 'select_province__Name_of_Province')
    list_per_page = 25
    exclude = ['author', 'last_modified_by', 'timestamp']
    autocomplete_fields = ['related_ministry', 'select_province']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="Federal_Executive").exists():
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class ProvinceJudiciaryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'select_province', 'court', 'category', 'last_modified_by',
        'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author__username', 'select_province__Name_of_Province')
    list_per_page = 25
    exclude = ['author', 'last_modified_by', 'timestamp']
    autocomplete_fields = ['select_province']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="Federal_Judiciary").exists():
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class ProvincialParliamentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'select_province', 'related_parliament', 'category',
        'last_modified_by', 'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author__username', 'select_province__Name_of_Province')
    list_per_page = 25
    exclude = ['author', 'last_modified_by', 'timestamp']
    autocomplete_fields = ['select_province']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="Federal_Judiciary").exists():
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class ProvincesNameAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'Name_of_Province')
    list_display_links = ('id', 'Name_of_Province')
    search_fields = ('Name_of_Province',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(ProvinceJudiciary, ProvinceJudiciaryAdmin)
admin.site.register(ProvinceExecutive, ProvinceExecutiveAdmin)
admin.site.register(ProvincialParliament, ProvincialParliamentAdmin)
admin.site.register(ProvincesName, ProvincesNameAdmin)
