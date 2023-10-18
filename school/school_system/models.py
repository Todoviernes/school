from django.db import models
from school.users.models import User
from school.utils.models import SystemModel, SlugModel


class Student(SystemModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    parent = models.ForeignKey(User, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Faculty(SystemModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name


class Staff(SystemModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name


class Parent(SystemModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')

    def __str__(self):
        return self.user.name


class Absence(SystemModel):
    student = models.ForeignKey(Student, related_name='absences', on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Absences"

    def __str__(self):
        return f"Absence on {self.date} for {self.student.first_name} {self.student.last_name}"


class Tardy(SystemModel):
    student = models.ForeignKey(Student, related_name='tardies', on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Tardy on {self.date} for {self.student.first_name} {self.student.last_name}"


class Excuse(SystemModel):
    student = models.ForeignKey(Student, related_name='excuses', on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField()
    provided_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Excuse on {self.date} for {self.student.first_name} {self.student.last_name}"


class Assignment(SystemModel):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Grade(SystemModel):
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.FloatField()
    total_points = models.FloatField()

    @property
    def percentage(self):
        return (self.score / self.total_points) * 100

    def __str__(self):
        return f"Grade for {self.assignment.title} by {self.student.first_name} {self.student.last_name}"


class Forum(SystemModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class ForumPost(SystemModel):
    forum = models.ForeignKey(Forum, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"Post by {self.author.name} on {self.created_at.date()}"
