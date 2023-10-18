from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from school.school_system.forms import (
    AbsenceForm,
    AssignmentForm,
    ExcuseForm,
    FacultyForm,
    ForumForm,
    ForumPostForm,
    GradeForm,
    StaffForm,
    StudentForm,
    TardyForm,
)
from school.school_system.models import (
    Absence,
    Assignment,
    Excuse,
    Faculty,
    Forum,
    ForumPost,
    Grade,
    Staff,
    Student,
    Tardy,
)

# Student Views


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = "students"
    template_name = "student_list.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("school_system:student-list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("school_system:student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("student-list")


# Faculty Views


class FacultyListView(ListView):
    model = Faculty
    template_name = "faculty_list.html"


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = "faculty_detail.html"


class FacultyCreateView(CreateView):
    model = Faculty
    form_class = FacultyForm
    template_name = "faculty_form.html"
    success_url = reverse_lazy("faculty-list")


class FacultyUpdateView(UpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = "faculty_form.html"
    success_url = reverse_lazy("faculty-list")


class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = "faculty_confirm_delete.html"
    success_url = reverse_lazy("faculty-list")


# Staff Views


class StaffListView(ListView):
    model = Staff
    template_name = "staff_list.html"


class StaffDetailView(DetailView):
    model = Staff
    template_name = "staff_detail.html"


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "staff_form.html"
    success_url = reverse_lazy("staff-list")


class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = "staff_form.html"
    success_url = reverse_lazy("staff-list")


class StaffDeleteView(DeleteView):
    model = Staff
    template_name = "staff_confirm_delete.html"
    success_url = reverse_lazy("staff-list")


# Absence Views


class AbsenceListView(ListView):
    model = Absence
    template_name = "absence_list.html"


class AbsenceDetailView(DetailView):
    model = Absence
    template_name = "absence_detail.html"


class AbsenceCreateView(CreateView):
    model = Absence
    form_class = AbsenceForm
    template_name = "absence_form.html"
    success_url = reverse_lazy("absence-list")


class AbsenceUpdateView(UpdateView):
    model = Absence
    form_class = AbsenceForm
    template_name = "absence_form.html"
    success_url = reverse_lazy("absence-list")


class AbsenceDeleteView(DeleteView):
    model = Absence
    template_name = "absence_confirm_delete.html"
    success_url = reverse_lazy("absence-list")


# Tardy Views


class TardyListView(ListView):
    model = Tardy
    template_name = "tardy_list.html"


class TardyDetailView(DetailView):
    model = Tardy
    template_name = "tardy_detail.html"


class TardyCreateView(CreateView):
    model = Tardy
    form_class = TardyForm
    template_name = "tardy_form.html"
    success_url = reverse_lazy("tardy-list")


class TardyUpdateView(UpdateView):
    model = Tardy
    form_class = TardyForm
    template_name = "tardy_form.html"
    success_url = reverse_lazy("tardy-list")


class TardyDeleteView(DeleteView):
    model = Tardy
    template_name = "tardy_confirm_delete.html"
    success_url = reverse_lazy("tardy-list")


# Excuse Views


class ExcuseListView(ListView):
    model = Excuse
    template_name = "excuse_list.html"


class ExcuseDetailView(DetailView):
    model = Excuse
    template_name = "excuse_detail.html"


class ExcuseCreateView(CreateView):
    model = Excuse
    form_class = ExcuseForm
    template_name = "excuse_form.html"
    success_url = reverse_lazy("excuse-list")


class ExcuseUpdateView(UpdateView):
    model = Excuse
    form_class = ExcuseForm
    template_name = "excuse_form.html"
    success_url = reverse_lazy("excuse-list")


class ExcuseDeleteView(DeleteView):
    model = Excuse
    template_name = "excuse_confirm_delete.html"
    success_url = reverse_lazy("excuse-list")


# Assignment Views


class AssignmentListView(ListView):
    model = Assignment
    template_name = "assignment_list.html"


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = "assignment_detail.html"


class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "assignment_form.html"
    success_url = reverse_lazy("assignment-list")


class AssignmentUpdateView(UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "assignment_form.html"
    success_url = reverse_lazy("assignment-list")


class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = "assignment_confirm_delete.html"
    success_url = reverse_lazy("assignment-list")


# Grade Views


class GradeListView(ListView):
    model = Grade
    template_name = "grade_list.html"


class GradeDetailView(DetailView):
    model = Grade
    template_name = "grade_detail.html"


class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = "grade_form.html"
    success_url = reverse_lazy("grade-list")


class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = "grade_form.html"
    success_url = reverse_lazy("grade-list")


class GradeDeleteView(DeleteView):
    model = Grade
    template_name = "grade_confirm_delete.html"
    success_url = reverse_lazy("grade-list")


# Forum Views


class ForumListView(ListView):
    model = Forum
    template_name = "forum_list.html"


class ForumDetailView(DetailView):
    model = Forum
    template_name = "forum_detail.html"


class ForumCreateView(CreateView):
    model = Forum
    form_class = ForumForm
    template_name = "forum_form.html"
    success_url = reverse_lazy("forum-list")


class ForumUpdateView(UpdateView):
    model = Forum
    form_class = ForumForm
    template_name = "forum_form.html"
    success_url = reverse_lazy("forum-list")


class ForumDeleteView(DeleteView):
    model = Forum
    template_name = "forum_confirm_delete.html"
    success_url = reverse_lazy("forum-list")


# ForumPost Views


class ForumPostListView(ListView):
    model = ForumPost
    template_name = "forumpost_list.html"


class ForumPostDetailView(DetailView):
    model = ForumPost
    template_name = "forumpost_detail.html"


class ForumPostCreateView(CreateView):
    model = ForumPost
    form_class = ForumPostForm
    template_name = "forumpost_form.html"
    success_url = reverse_lazy("forumpost-list")


class ForumPostUpdateView(UpdateView):
    model = ForumPost
    form_class = ForumPostForm
    template_name = "forumpost_form.html"
    success_url = reverse_lazy("forumpost-list")


class ForumPostDeleteView(DeleteView):
    model = ForumPost
    template_name = "forumpost_confirm_delete.html"
    success_url = reverse_lazy("forumpost-list")
