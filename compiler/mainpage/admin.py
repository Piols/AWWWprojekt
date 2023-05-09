from django.contrib import admin

from .models import File, Folder

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'parent_folder', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('owner', 'parent_folder')

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'parent_folder', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('owner', 'parent_folder')

admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)