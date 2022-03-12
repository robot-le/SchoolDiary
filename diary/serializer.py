from rest_framework import serializers

from diary.models import Student, Subject, Grade, Group


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'group', 'mentor', 'mentee']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = '__all__'
