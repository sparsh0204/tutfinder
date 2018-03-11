from rest_framework import serializers
from .models import Technology
#from django.contrib.auth.models import User


class TechnologySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
#    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Technology
        fields = ('title', 'details', 'doc_url', 'logo', 'logo_url', 'slug')
#        read_only_fields = ('created',)

'''class UserSerializer(serializers.ModelSerializer):
    photos = serializers.PrimaryKeyRelatedField(many=True, queryset=Photos.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'photos')'''
