from django.urls import path

from .views import (
    TaskCreateView, # create a new task
    TaskView, # get all tasks
    TaskUpdateView, # update a task by id
    TaskDeleteView, # delete a task by id
    AssignmentCreateView, # create a new assignment
    AssignmentView, # get all assignments or get an assignment by id
    AssignmentUpdateView, # update an assignment by id
    AssignmentDeleteView, # delete an assignment by id

    LessonView, # get all lessons or get lesson by group id
    LessonCreateView, # create lesson,
    SubmissionCreateView, # create submission
    GetResultView, # get result by goup id and lesson id, assignment id
)


urlpatterns = [
    path('task/add/', TaskCreateView.as_view()), # add task
    path('task/all/', TaskView.as_view()), # get all tasks
    path('task/update/<int:pk>/', TaskUpdateView.as_view()), # update task by id
    path('task/delete/<int:pk>/', TaskDeleteView.as_view()), # delete task by id
    path('assignment/add/', AssignmentCreateView.as_view()), # add assignment
    path('assignment/all/', AssignmentView.as_view()), # get all assignments
    path('assignment/<int:pk>/', AssignmentView.as_view()), # get assignment by id
    path('assignment/update/<int:pk>/', AssignmentUpdateView.as_view()), # update assignment by id
    path('assignment/delete/<int:pk>/', AssignmentDeleteView.as_view()), # delete assignment by id

    path('get/<int:pk>/', LessonView.as_view()), # get lesson by group id
    path('add/', LessonCreateView.as_view()), # create lesson

    path('submission/add/', SubmissionCreateView.as_view()), # create submission
    path('result/', GetResultView.as_view()), # get result by goup id and lesson id, assignment id
]