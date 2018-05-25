from rest_framework import serializers

from course.models import Course
from review.models import Review
from technology.models import Technology
from user.models import Profile


# from django.contrib.auth.models import User


class TechnologySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    #    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Technology
        fields = ('id', 'title', 'details', 'doc_url', 'logo', 'logo_url', 'slug')


#        read_only_fields = ('created',)
class CourseSerializer(serializers.ModelSerializer):
    tech = serializers.StringRelatedField()
    submitter = serializers.StringRelatedField()
    tutor = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ('id', 'submitter', 'tutor', 'logo_url', 'url', 'title', 'detail', 'free', 'level', 'upvotes', 'tech', 'slug')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'course', 'text', 'upvotes')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
