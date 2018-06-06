from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from .models import TrackCourse
# from django.contrib.auth.models import User


track_course_detail_url = HyperlinkedIdentityField(
    view_name = 'track_course:track_course_detail', #related name in urls
    lookup_field = 'slug'
)

class TrackCourseCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = TrackCourse
        fields = [
            'track',
            'tutor',
            'title',
            'detail',
            'logo',
            'logo_url',
            'medium',
            'free',
            'level',
        ]
    #def get_track(self, obj):
    #    return str(obj.track.title)
    #def get_tutor(self, obj):
    #    return str(obj.tutor.username)

class TrackCourseListSerializer(ModelSerializer):
    # url = track_course_detail_url
    track = SerializerMethodField()
    # tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = TrackCourse
        fields = [
            'id',
            'number',
            'track',
            # 'tutor',
            'title',
            'slug',
            'url',
            'detail',
            'image',
            'logo',
            'logo_url',
            'medium',
            'free',
            'level',
        ]
    def get_track(self, obj):
        return str(obj.track.title)
    # def get_tutor(self, obj):
    #     return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class TrackCourseDetailSerializer(ModelSerializer):
    track = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = TrackCourse
        fields = [
            'id',
            'track',
            'tutor',
            'title',
            'slug',
            'detail',
            'image',
            'logo',
            'logo_url',
            'medium',
            'free',
            'level',
        ]
    def get_track(self, obj):
        return str(obj.track.title)

    def get_tutor(self, obj):
        return str(obj.tutor.username)

    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class TrackCourseDeleteSerializer(ModelSerializer):
    track = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = TrackCourse
        fields = [
            'track',
            'tutor',
            'title',
            'detail',
            'image',
            'logo',
            'logo_url',
            'medium',
            'free',
            'level',
        ]
    def get_track(self, obj):
        return str(obj.track.title)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image
