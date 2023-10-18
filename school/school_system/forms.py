from django import forms
from school.school_system.models import Student, Faculty, Staff, Absence, Tardy, Excuse, Assignment, Grade, Forum, ForumPost


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = '__all__'


class TardyForm(forms.ModelForm):
    class Meta:
        model = Tardy
        fields = '__all__'


class ExcuseForm(forms.ModelForm):
    class Meta:
        model = Excuse
        fields = '__all__'


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = '__all__'
