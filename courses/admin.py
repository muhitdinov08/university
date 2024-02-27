from django.contrib import admin
from .models import Teacher, Speciality, Subject


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = ("degree",)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "code")
    search_fields = ("name", "code")
    list_filter = ("is_active",)
    prepopulated_fields = {
        'slug': ["start_date", 'name'],
    }


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "created_at")
    autocomplete_fields = ("speciality",)
