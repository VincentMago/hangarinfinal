from django.contrib import admin

# Register your models here.
from .models import Priority, Category, Task, Note, SubTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
        list_display = ('title', 'status', 'priority', 'category', 'deadline')
        list_filter = ('status', 'priority', 'category')
        search_fields = ('title', 'description')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
        list_display = ('title', 'status', 'parent_task')
        list_filter = ('status', 'parent_task')
        search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
