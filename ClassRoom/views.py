from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import (
    StudentStatus,
    Student,
    TeacherType,
    Teacher,
    Course,
    Group,
)

from .serializers import (
    StudentStatusSerializer,
    StudentSerializer,
    TeacherTypeSerializer,
    TeacherSerializer,
    CourseSerializer,
    GroupSerializer,
)


class HomeView(APIView):
    def get(self, request: Request) -> Response:
        '''resturn welcome message'''
        return Response({'status': 'welcome to student api'})


class StudentView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        '''get student by id'''
        try:
            student = Student.objects.get(id=pk) # get student by id
            serializer = StudentSerializer(student) # serialize student
            return Response(serializer.data) # return student
        except ObjectDoesNotExist:
            return Response({'status': 'student does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message


class StudentCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''create new student'''
        data = request.data # get data from request
        serializer = StudentSerializer(data=data) # serialize data
        if serializer.is_valid():
            serializer.save() # save student
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return student
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message


class StudentUpdateView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''update student by id'''
        try:
            student = Student.objects.get(id=pk) # get student by id
            serializer = StudentSerializer(student, data=request.data) # serialize data
            if serializer.is_valid():
                serializer.save() # save student
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # return student
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message
        except ObjectDoesNotExist:
            return Response({'status': 'student does not exist'}, status=status.HTTP_404_NOT_FOUND)


class StudentDeleteView(APIView):  
    def post(self, request: Request, pk: int) -> Response:
        '''delete student by id'''
        try:
            student = Student.objects.get(id=pk) # get student by id
            student.delete() # delete student
            return Response({'status': 'student deleted'}, status=status.HTTP_204_NO_CONTENT) # return success message
        except ObjectDoesNotExist:
            return Response({'status': 'student does not exist'}, status=status.HTTP_404_NOT_FOUND)


class StudentsView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        '''get students by group id'''
        if pk is not None:
            try:
                group = Group.objects.get(id=pk) # get group by id
                students = group.students.all() # get students by group
                serializer = StudentSerializer(students, many=True) # serialize students
                return Response(serializer.data) # return students
            except ObjectDoesNotExist:
                return Response({'status': 'group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all() # get all students
            serializer = StudentSerializer(students, many=True) # serialize students
            return Response(serializer.data) # return students


class CourseView(APIView):
    def get(self, request: Request) -> Response:
        '''get all courses'''
        courses = Course.objects.all() # get all courses
        serializer = CourseSerializer(courses, many=True) # serialize courses
        return Response(serializer.data) # return courses


class CourseCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''create new course'''
        data = request.data # get data from request
        serializer = CourseSerializer(data=data) # serialize data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseUpdateView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''update course by id'''
        try:
            course = Course.objects.get(id=pk) # get course by id
            serializer = CourseSerializer(course, data=request.data) # serialize data
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'status': 'course does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CourseDeleteView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''delete course by id'''
        try:
            course = Course.objects.get(id=pk) # get course by id
            course.delete() # delete course
            return Response({'status': 'course deleted'}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({'status': 'course does not exist'}, status=status.HTTP_404_NOT_FOUND)


class GroupView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        '''get group by course id'''
        try:
            groups = Group.objects.filter(course=pk)
            serializer = GroupSerializer(groups, many=True) # serialize groups
            return Response(serializer.data) # return groups
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND) # return error message
        

class GroupCreateView(APIView):
    def post(self, request: Request) -> Response:
        '''create new group'''
        data = request.data # get data from request
        serializer = GroupSerializer(data=data) # serialize data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return group
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message


class GroupUpdateView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''update group by id'''
        try:
            group = Group.objects.get(id=pk) # get group by id
            serializer = GroupSerializer(group, data=request.data) # serialize data
            if serializer.is_valid():
                serializer.save() # save group
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # return group
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message
        except ObjectDoesNotExist:
            return Response({'status': 'group does not exist'}, status=status.HTTP_404_NOT_FOUND)# return error message


class GroupDeleteView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''delete group by id'''
        try:
            group = Group.objects.get(id=pk) # get group by id
            group.delete() # delete group
            return Response({'status': 'group deleted'}, status=status.HTTP_204_NO_CONTENT) # return success message
        except ObjectDoesNotExist:
            return Response({'status': 'group does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message


class AddStudentsToGroupView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''add students to group by group id'''
        try:
            group = Group.objects.get(id=pk) # get group by id
            students = request.data['students'] # get students from request
            for student in students:
                try:
                    student = Student.objects.get(id=student) # get student by id
                    group.students.add(student) # add student to group
                except ObjectDoesNotExist:
                    return Response({'status': 'student does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message
            return Response({'status': 'students added'}, status=status.HTTP_202_ACCEPTED) # return success message
        except ObjectDoesNotExist:
            return Response({'status': 'group does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message


class RemoveStudentsFromGroupView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        '''remove students from group by group id'''
        try:
            group = Group.objects.get(id=pk) # get group by id
            students = request.data['students'] # get students from request
            for student in students:
                try:
                    student = Student.objects.get(id=student) # get student by id
                    group.students.remove(student) # remove student from group
                except ObjectDoesNotExist:
                    return Response({'status': 'student does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message
            return Response({'status': 'students removed'}, status=status.HTTP_202_ACCEPTED) # return success message
        except ObjectDoesNotExist:
            return Response({'status': 'group does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message


class GetStudentsfromGroupView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        '''get students from group by group id'''
        try:
            group = Group.objects.get(id=pk) # get group by id
            students = group.students.all() # get students from group
            serializer = StudentSerializer(students, many=True) # serialize students
            return Response(serializer.data) # return students
        except ObjectDoesNotExist:
            return Response({'status': 'group does not exist'}, status=status.HTTP_404_NOT_FOUND) # return error message   

class CreateTypeTeacher(APIView):
    def post(self, request: Request) -> Response:
        '''create new type teacher'''
        data = request.data # get data from request
        serializer = TeacherTypeSerializer(data=data) # serialize data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return type teacher
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message
    def get(self, request: Request) -> Response:
        '''get all type teacher'''
        type_teacher = TeacherType.objects.all()
        serializer = TeacherTypeSerializer(type_teacher, many=True) # serialize type teacher
        return Response(serializer.data) # return type teacher
    def put (self, request: Request, pk: int) -> Response:
        '''update type teacher by id'''
        try:
            type_teacher = TeacherType.objects.get(id=pk) # get type teacher by id
            serializer = TeacherTypeSerializer(type_teacher, data=request.data) # serialize data
            if serializer.is_valid():
                serializer.save() # save type teacher
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # return type teacher
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message
        except ObjectDoesNotExist:
            return Response({'status': 'type teacher does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

class CreateTeacher(APIView):
    def post(self, request: Request) -> Response:
        '''create new teacher'''
        data = request.data # get data from request
        serializer = TeacherSerializer(data=data) # serialize data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return teacher
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message
    def get(self, request: Request) -> Response:
        '''get all teacher'''
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True) # serialize teacher
        return Response(serializer.data) # return teacher
    def put (self, request: Request, pk: int) -> Response:
        '''update teacher by id'''
        try:
            teacher = Teacher.objects.get(id=pk) # get teacher by id
            serializer = TeacherSerializer(teacher, data=request.data) # serialize data
            if serializer.is_valid():
                serializer.save() # save teacher
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # return teacher
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return error message
        except ObjectDoesNotExist:
            return Response({'status': 'teacher does not exist'}, status=status.HTTP_404_NOT_FOUND)
    