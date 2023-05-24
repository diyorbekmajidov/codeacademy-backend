from django.urls import path
from .views import (
    HomeView,
    StudentView, # get student by id
    StudentCreateView, # create student   
    StudentUpdateView, # update student
    StudentDeleteView, # delete student
    StudentsView, # get all students or get student by group id
    CourseView, # get all courses
    CourseCreateView, # create course
    CourseUpdateView, # update course
    CourseDeleteView, # delete course
    GroupView, # get all groups or get groups by course id
    GroupCreateView, # create group
    GroupUpdateView, # update group
    GroupDeleteView, # delete group
    AddStudentsToGroupView, # add student to group
    RemoveStudentsFromGroupView, # remove student from group
    GetStudentsfromGroupView, # get students from group
    CreateTypeTeacher , # create type teacher
    CreateTeacher,  # create teacher
    GetTeacherType, # get teacher type
    GetTeacher, # get teacher

)


urlpatterns = [
    path('', HomeView.as_view()), # welcome message
    path('student/<int:pk>/', StudentView.as_view()), # get student by id
    path('student/add/', StudentCreateView.as_view()), # create student
    path('student/update/<int:pk>/', StudentUpdateView.as_view()), # update student
    path('student/delete/<int:pk>/', StudentDeleteView.as_view()), # delete student
    path('student/all/', StudentsView.as_view()), # get all students
    path('students/<int:pk>/', StudentsView.as_view()), # get student by group id
    path('course/', CourseView.as_view()), # get all courses
    path('course/add/', CourseCreateView.as_view()), # create course
    path('course/update/<int:pk>/', CourseUpdateView.as_view()), # update course
    path('course/delete/<int:pk>/', CourseDeleteView.as_view()), # delete course
    path('group/all/', GroupView.as_view()), # get all groups
    path('group/<int:pk>/', GroupView.as_view()), # get groups by course id
    path('group/add/', GroupCreateView.as_view()), # create group
    path('group/update/<int:pk>/', GroupUpdateView.as_view()), # update group
    path('group/delete/<int:pk>/', GroupDeleteView.as_view()), # delete group
    path('add-students-to-group/<int:pk>/', AddStudentsToGroupView.as_view()), # add student to group
    path('remove-students-from-group/<int:pk>/', RemoveStudentsFromGroupView.as_view()), # remove student from group
    path('get-students-from-group/<int:pk>/', GetStudentsfromGroupView.as_view()), # get students from group
    path('create-type-teacher/', CreateTypeTeacher.as_view()), # create type teacher
    path('create-type-teacher/<int:pk>/', CreateTypeTeacher.as_view()), # Update type teacher
    path('create-teacher/', CreateTeacher.as_view()), # create teacher
    path('create-teacher/<int:pk>/', CreateTeacher.as_view()), # update teacher
    path('get-teacher-type/<int:pk>/', GetTeacherType.as_view()), # get teacher type by id
    path('get-teacher/<int:pk>/', GetTeacher.as_view()), # get teacher by id
]