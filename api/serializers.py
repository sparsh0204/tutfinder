from rest_framework import serializers
from technology.models import Technology
from course.models import Course
from review.models import Review
#from django.contrib.auth.models import User


class TechnologySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
#    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Technology
        fields = ('title', 'details', 'doc_url', 'logo', 'logo_url', 'slug')
#        read_only_fields = ('created',)
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('user', 'url', 'title', 'free', 'level', 'upvotes', 'tech', 'slug')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('user', 'course', 'text', 'upvotes')