from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
admin.site.site_header = 'Layvio Admin'
admin.site.site_title = 'Layvio Admin'
admin.site.index_title = 'Layvio Admin'
# Register your models here.
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ['first_name', 'last_name', 'email']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

# class MyUserAdmin(admin.ModelAdmin):

#     list_display = [
#         'name', 'email', 'phone'
#     ]
#     search_fields = [
#         'name', 'email', 'phone'
#     ]



#     # actions = [custom_action,]

#admin.site.register(User, UserAdmin)

admin.site.register(StaticPages)


class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name','image','slug','status','created_at']

    #search_fields = ['name', 'category__name']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
admin.site.register(Industry,IndustryAdmin)

class SubIndustryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','status','created_at']

    #search_fields = ['name', 'category__name']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
admin.site.register(SubIndustry,SubIndustryAdmin)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name','industry','image','template_type','slug','created_at']

    search_fields = ['name', 'industry__name','template_type']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
admin.site.register(Template,TemplateAdmin)
