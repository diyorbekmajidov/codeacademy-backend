from rest_framework import serializers

from .models import (
    AssignmentType,
    Assignment,
    TaskLevel,
    Task,
    Lesson,
    Muster,
    Submission,
)


class AssignmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentType
        fields = '__all__'
    

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class TaskLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLevel
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class MusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muster
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class GetAssignmentSerializer(serializers.ModelSerializer):
    type = AssignmentTypeSerializer()
    class Meta:
        model = Assignment
        fields = ('id', 'name', 'description', 'course', 'link', 'type', 'date_created', 'date_updated')