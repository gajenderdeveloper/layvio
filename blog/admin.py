from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_at']

    search_fields = ['title']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
admin.site.register(Post,PostAdmin)
