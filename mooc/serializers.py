from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Lecture, Homework


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ['url', 'name', 'description', 'slide']


class HomeworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homework
        fields = ['url', 'name', 'description', 'slide']

