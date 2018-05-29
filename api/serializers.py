from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from technology.models import Technology
from course.models import Course
#from review.models import Review
#from user.models import Profile
# from django.contrib.auth.models import User

tech_detail_url = HyperlinkedIdentityField(
    view_name = 'api:tech_detail', #related name in urls
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


course_detail_url = HyperlinkedIdentityField(
    view_name = 'api:course_detail', #related name in urls
    lookup_field = 'slug'
)

class CourseCreateUpdateSerializer(ModelSerializer):
    # tech = SerializerMethodField()
    submitter = SerializerMethodField()
    #tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'tech',
            'submitter',
            'tutor',
            'title',
            'detail',
            'image',
            'logo',
            'logo_url',
            'free',
            'level',
        ]
    #def get_tech(self, obj):
    #    return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    #def get_tutor(self, obj):
    #    return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class CourseListSerializer(ModelSerializer):
    url = course_detail_url
    tech = SerializerMethodField()
    submitter = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'id',
            'tech',
            'submitter',
            'tutor',
            'title',
            'slug',
            'url',
            'detail',
            'image',
            'logo',
            'logo_url',
            'upvotes',
            'free',
            'level',
        ]
    def get_tech(self, obj):
        return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class CourseDetailSerializer(ModelSerializer):
    tech = SerializerMethodField()
    submitter = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'id',
            'tech',
            'submitter',
            'tutor',
            'title',
            'slug',
            'url',
            'detail',
            'image',
            'logo',
            'logo_url',
            'upvotes',
            'free',
            'level',
        ]
    def get_tech(self, obj):
        return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class CourseDeleteSerializer(ModelSerializer):
    tech = SerializerMethodField()
    submitter = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'tech',
            'submitter',
            'tutor',
            'title',
            'detail',
            'image',
            'logo',
            'logo_url',
            'free',
            'level',
        ]
    def get_tech(self, obj):
        return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

# class ReviewSerializer(ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('user', 'course', 'text', 'upvotes')
#
#
# class ProfileSerializer(ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
