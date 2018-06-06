from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from .models import Technology
# from django.contrib.auth.models import User

tech_detail_url = HyperlinkedIdentityField(
    view_name = 'tech:tech_detail', #related name in urls
    lookup_field = 'slug'
)

class TechnologyCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = [
            'title',
            'detail',
            'doc_url',
            'logo',
            'logo_url',
        ]

class TechnologyListSerializer(ModelSerializer):
    url = tech_detail_url
    image = SerializerMethodField()
    class Meta:
        model = Technology
        fields = [
            'id',
            'url',
            'title',
            'slug',
            'detail',
            'image',
            'doc_url',
            'logo',
            'logo_url',
            'course_count',
        ]
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class TechnologyDetailSerializer(ModelSerializer):
    image = SerializerMethodField()
    class Meta:
        model = Technology
        fields = [
            'id',
            'title',
            'slug',
            'detail',
            'image',
            'doc_url',
            'logo',
            'logo_url',
            'course_count',
        ]
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class TechnologyDeleteSerializer(ModelSerializer):
    image = SerializerMethodField()
    class Meta:
        model = Technology
        fields = [
            'id',
            'title',
            'slug',
            'detail',
            'image',
            'doc_url',
            'logo',
            'logo_url',
        ]
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image
