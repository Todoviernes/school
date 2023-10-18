from django.contrib import admin
from .models import (Student, Faculty, Staff, Absence, Tardy,
                     Excuse, Assignment, Grade, Forum, ForumPost)

# Tabular Inlines


class AbsenceInline(admin.TabularInline):
    model = Absence
    extra = 0


class TardyInline(admin.TabularInline):
    model = Tardy
    extra = 0


class ExcuseInline(admin.TabularInline):
    model = Excuse
    extra = 0


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 0


class ForumPostInline(admin.TabularInline):
    model = ForumPost
    extra = 0

# Admin models


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'enrollment_date', 'parent', 'created']
    inlines = [AbsenceInline, TardyInline, ExcuseInline, GradeInline]
    search_fields = ['first_name', 'last_name', 'parent__name']
    list_filter = ['enrollment_date']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user__name', 'title']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'position']
    search_fields = ['user__name', 'position']


@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'reason', 'recorded_by']
    search_fields = ['student__first_name', 'student__last_name', 'reason']


@admin.register(Tardy)
class TardyAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'reason', 'recorded_by']
    search_fields = ['student__first_name', 'student__last_name', 'reason']


@admin.register(Excuse)
class ExcuseAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'note', 'provided_by']
    search_fields = ['student__first_name', 'student__last_name', 'note']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date']
    search_fields = ['title', 'description']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'assignment', 'score', 'total_points', 'percentage']
    search_fields = ['student__first_name', 'student__last_name', 'assignment__title']


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [ForumPostInline]
    search_fields = ['title', 'description']


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ['forum', 'author', 'created']
    search_fields = ['forum__title', 'author__name', 'content']
