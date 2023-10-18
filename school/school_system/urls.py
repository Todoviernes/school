from django.urls import path
from school.school_system.views import (
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    AbsenceListView, AbsenceDetailView, AbsenceCreateView, AbsenceUpdateView, AbsenceDeleteView,
    TardyListView, TardyDetailView, TardyCreateView, TardyUpdateView, TardyDeleteView,
    ExcuseListView, ExcuseDetailView, ExcuseCreateView, ExcuseUpdateView, ExcuseDeleteView,
    AssignmentListView, AssignmentDetailView, AssignmentCreateView, AssignmentUpdateView, AssignmentDeleteView,
    GradeListView, GradeDetailView, GradeCreateView, GradeUpdateView, GradeDeleteView,
    ForumListView, ForumDetailView, ForumCreateView, ForumUpdateView, ForumDeleteView,
    ForumPostListView, ForumPostDetailView, ForumPostCreateView, ForumPostUpdateView, ForumPostDeleteView
)
app_name = "school_system"

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # Absence URLs
    path('absences/', AbsenceListView.as_view(), name='absence-list'),
    path('absences/<int:pk>/', AbsenceDetailView.as_view(), name='absence-detail'),
    path('absences/create/', AbsenceCreateView.as_view(), name='absence-create'),
    path('absences/<int:pk>/update/', AbsenceUpdateView.as_view(), name='absence-update'),
    path('absences/<int:pk>/delete/', AbsenceDeleteView.as_view(), name='absence-delete'),

    # Tardy URLs
    path('tardies/', TardyListView.as_view(), name='tardy-list'),
    path('tardies/<int:pk>/', TardyDetailView.as_view(), name='tardy-detail'),
    path('tardies/create/', TardyCreateView.as_view(), name='tardy-create'),
    path('tardies/<int:pk>/update/', TardyUpdateView.as_view(), name='tardy-update'),
    path('tardies/<int:pk>/delete/', TardyDeleteView.as_view(), name='tardy-delete'),

    # Excuse URLs
    path('excuses/', ExcuseListView.as_view(), name='excuse-list'),
    path('excuses/<int:pk>/', ExcuseDetailView.as_view(), name='excuse-detail'),
    path('excuses/create/', ExcuseCreateView.as_view(), name='excuse-create'),
    path('excuses/<int:pk>/update/', ExcuseUpdateView.as_view(), name='excuse-update'),
    path('excuses/<int:pk>/delete/', ExcuseDeleteView.as_view(), name='excuse-delete'),

    # Assignment URLs
    path('assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignments/create/', AssignmentCreateView.as_view(), name='assignment-create'),
    path('assignments/<int:pk>/update/', AssignmentUpdateView.as_view(), name='assignment-update'),
    path('assignments/<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment-delete'),

    # Grade URLs
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('grades/<int:pk>/', GradeDetailView.as_view(), name='grade-detail'),
    path('grades/create/', GradeCreateView.as_view(), name='grade-create'),
    path('grades/<int:pk>/update/', GradeUpdateView.as_view(), name='grade-update'),
    path('grades/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade-delete'),

    # Forum URLs
    path('forums/', ForumListView.as_view(), name='forum-list'),
    path('forums/<int:pk>/', ForumDetailView.as_view(), name='forum-detail'),
    path('forums/create/', ForumCreateView.as_view(), name='forum-create'),
    path('forums/<int:pk>/update/', ForumUpdateView.as_view(), name='forum-update'),
    path('forums/<int:pk>/delete/', ForumDeleteView.as_view(), name='forum-delete'),

    # ForumPost URLs
    path('forum-posts/', ForumPostListView.as_view(), name='forum-post-list'),
    path('forum-posts/<int:pk>/', ForumPostDetailView.as_view(), name='forum-post-detail'),
    path('forum-posts/create/', ForumPostCreateView.as_view(), name='forum-post-create'),
    path('forum-posts/<int:pk>/update/', ForumPostUpdateView.as_view(), name='forum-post-update'),
    path('forum-posts/<int:pk>/delete/', ForumPostDeleteView.as_view(), name='forum-post-delete'),
]
