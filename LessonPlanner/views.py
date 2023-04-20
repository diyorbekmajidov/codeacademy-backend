from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from .models import (
    AssignmentType,
    Assignment,
    TaskLevel,
    Task,
    Lesson,
    Muster,
    Submission,
)

from ClassRoom.models import (
    Student,
    Group,
    Course,
)

from .serializers import (
    TaskSerializer, 
    AssignmentSerializer,
    LessonSerializer,
    SubmissionSerializer,
    GetAssignmentSerializer,
)


class TaskCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''Create a new task'''
        data = request.data # get data from request
        try:
            if data.get('assignment') is None or data.get('level') is None or data.get('course') is None:
                return Response(status=status.HTTP_400_BAD_REQUEST) # return error and status code
            course = Course.objects.get(name=data['course'])
            assignment = Assignment.objects.get(name=data['assignment'], course=course) # get assignment by id
            data['assignment'] = assignment.pk # set assignment to assignment object
            level = TaskLevel.objects.get(name=data['level']) # get level by id
            data['level'] = level.pk # set level to level object
            serializer = TaskSerializer(data=data) # create serializer
            if serializer.is_valid(): # check if data is valid
                serializer.save() # save data to database
                return Response(serializer.data, status=status.HTTP_201_CREATED) # return data and status code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return errors and status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code


class TaskView(APIView):
    def get(self, request: Request) -> Response:
        '''Get all tasks'''
        tasks = Task.objects.all() # get all tasks
        serializer = TaskSerializer(tasks, many=True) # create serializer
        return Response(serializer.data, status=status.HTTP_200_OK) # return data and status code


class TaskUpdateView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''Update a task by id'''
        data = request.data # get data from request
        try:
            task = Task.objects.get(pk=pk) # get task by id
            data['assignment'] = pk # set assignment to assignment object
            if data.get('level') is not None:
                level = TaskLevel.objects.get(name=data['level']) # get level by id
                data['level'] = level.pk # set level to level object
            serializer = TaskSerializer(task, data=data) # create serializer
            if serializer.is_valid(): # check if data is valid
                serializer.save() # save data to database
                return Response(serializer.data, status=status.HTTP_200_OK) # return data and status code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return errors and status code 
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
        

class TaskDeleteView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''Delete a task by id'''
        try:
            task = Task.objects.get(pk=pk) # get task by id
            task.delete() # delete task
            return Response(status=status.HTTP_204_NO_CONTENT) # return status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
        

class AssignmentCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''Create a new assignment'''
        data = request.data # get data from request
        serializer = AssignmentSerializer(data=data) # create serializer
        if serializer.is_valid(): # check if data is valid
            serializer.save() # save data to database
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return data and status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return errors and status code


class AssignmentView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        '''Get assignments by lesson id'''
        try:
            lesson = Lesson.objects.get(id=pk) # get lesson by id
            assignments = lesson.assignments.all() # get all assignments by lesson id
            serializer = GetAssignmentSerializer(assignments, many=True) # create serializer
            return Response(serializer.data, status=status.HTTP_200_OK) # return data and status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code 
    

class AssignmentUpdateView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''Update an assignment by id'''
        data = request.data # get data from request
        try:
            assignment = Assignment.objects.get(pk=pk) # get assignment by id
            if data.get('type') is not None:
                assignment_type = AssignmentType.objects.get(name=data['type']) # get assignment type by id
                data['type'] = assignment_type.pk # set type to assignment type object
            if data.get('name') is not None:
                data['link'] = f'https://github.com/Final-PythonFoundationHomework/{data["name"]}'
            serializer = AssignmentSerializer(assignment, data=data) # create serializer
            if serializer.is_valid(): # check if data is valid
                serializer.save() # save data to database
                return Response(serializer.data, status=status.HTTP_200_OK) # return data and status code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return errors and status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
    

class AssignmentDeleteView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''Delete an assignment by id'''
        try:
            assignment = Assignment.objects.get(pk=pk) # get assignment by id
            assignment.delete() # delete assignment
            return Response(status=status.HTTP_204_NO_CONTENT) # return status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
        

class LessonCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''Create a new lesson'''
        data = request.data # get data from request
        try:
            serializer = LessonSerializer(data=data) # create serializer
            if serializer.is_valid(): # check if data is valid
                serializer.save() # save data to database
                return Response(serializer.data, status=status.HTTP_201_CREATED) # return data and status code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return errors and status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code


class LessonView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        '''Get lessons by group id'''
        try:
            lessons = Lesson.objects.filter(group=pk) # get lessons by group id
            serializer = LessonSerializer(lessons, many=True) # create serializer
            return Response(serializer.data, status=status.HTTP_200_OK) # return data and status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
        


class SubmissionCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''Create a new submission'''
        data = request.data # get data from request
        {
            'github': 'djumanov',
            'assignment': 'list_search',
            'course': 'Python Foundation',
            'tasks': [
                {
                    'isSolved': False,
                    'name': 'find01_max'
                }
            ]
        }

        try:
            student = Student.objects.get(github=data['github']) # get student by github
            course = Course.objects.get(name=data['course']) # get course by name
            assignment = Assignment.objects.get(name=data['assignment'], course=course) # get assignment by name and course
            for task in data['tasks']:
                task_object = Task.objects.get(name=task['name'], assignment=assignment) # get task by name and assignment
                submission = Submission.objects.create(student=student, task=task_object, is_correct=task['isSolved'], assignment=assignment) # create submission
            return Response(status=status.HTTP_201_CREATED) # return status code
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
        

class GetResultView(APIView):
    def post(self, request: Request) -> Response:
        '''get results by lesson id and assignment id'''
        data = request.data # get data from request
        try:
            lesson = Lesson.objects.get(id=data.get('lesson'))
            group = lesson.group
            assignment: Assignment = lesson.assignments.get(id=data.get('assignment'))
            tasks = Task.objects.filter(assignment=assignment)

            # print(group.student.all())
            students = group.students.all()
            results = []
            for student in students:
                result = []
                for problem in tasks:
                    submission = Submission.objects.filter(student=student, task=problem)
                    if submission.last():
                        result.append({
                            'id': problem.id,
                            'name': problem.name,
                            'is_correct': submission.last().is_correct,
                            'attempt': submission.count()
                        })
                    else:
                        result.append({
                            'id': problem.id,
                            'name': problem.name,
                            'is_correct': False,
                            'attempt': 0
                        })
        
                results.append({
                    'student': student.full_name,
                    'attempt': sum([i['attempt'] for i in result]),
                    'result': result
                })
                
            # return Response({'results': sorted(results, key=lambda x: len(x['result']), reverse=True)})
            return Response(results)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # return error and status code
