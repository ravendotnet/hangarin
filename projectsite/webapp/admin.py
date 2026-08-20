from django.contrib import admin

from .models import Priority, Category, Task, Note, SubTask
# Register your models here.

#admin.site.register(Priority)
#admin.site.register(Category)
#admin.site.register(Task)
#admin.site.register(Note)
#admin.site.register(SubTask)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "deadline", "status", "priority", "category",)
    search_fields = ("title","description",)
    list_filter = ("status", "priority", "category",)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "parent_task_name",)
    search_fields = ("title",)
    list_filter =("status",)

    def parent_task_name(self, obj):
        return obj.parent_task.title

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "content", "created_at",)
    search_fields = ("content",)
    list_filter = ("created_at",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

