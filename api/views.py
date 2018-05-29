#from rest_framework import status
from django.db.models import Q
#from django.contrib.auth.models import User
#from django.shortcuts import render
#from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from .serializers import (
    TechnologyListSerializer,
    TechnologyDetailSerializer,
    TechnologyCreateUpdateSerializer,
    TechnologyDeleteSerializer,
    CourseListSerializer,
    CourseDetailSerializer,
    CourseCreateUpdateSerializer,
    CourseDeleteSerializer,
    # ReviewSerializer,
    # ProfileSerializer,
)
from technology.models import Technology
from course.models import Course
# from review.models import Review
# from user.models import Profile


class TechnologyCreateAPIView(CreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class TechnologyListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = TechnologyListSerializer
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Technology.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(detail__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
                ).distinct()
        return queryset_list

class TechnologyDetailAPIView(RetrieveAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyDetailSerializer
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TechnologyDeleteAPIView(DestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyDeleteSerializer
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TechnologyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_url_kwrg = 'slug'

class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(submitter=self.request.user)

class CourseListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Course.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(detail__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)|
                Q(tech__title__icontains=query)
                ).distinct()
        return queryset_list

class CourseTechListAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    filter_backends = [SearchFilter, OrderingFilter]  # ordering=title in url (-title gives opposite)
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        tech_slug = self.kwargs['tech_slug']
        return Course.objects.filter(tech__slug = tech_slug)

class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class CourseDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDeleteSerializer
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class CourseUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_url_kwrg = 'slug'



# class TechnologyList(generics.ListCreateAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer
#
#
# class TechnologyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer


# class TechCourseList(generics.ListCreateAPIView):
#     serializer_class = CourseSerializer
#
#     def get_queryset(self):
#         tech = self.kwargs['tech']
#         return Course.objects.filter(tech__title=tech)


# class CourseList(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseDetail(generics.ListCreateAPIView):
#     # queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#     def get_queryset(self):
#         slug = self.kwargs['slug']
#         return Course.objects.filter(slug=slug)
#
# class TechCourseList(generics.ListCreateAPIView):
#     serializer_class = CourseSerializer
#
#     def get_queryset(self):
#         tech = self.kwargs['tech']
#         return Course.objects.filter(tech__title=tech)
#
# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get_queryset(self):
#         course = self.kwargs['course']
#         return Review.objects.filter(course=course)
#
# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer




'''class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
So far, so good. It looks pretty similar to the previous case, but we've got better separation between the different HTTP methods. We'll also need to update the instance view in views.py.

class CourseListView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, slug=None, format=None):
        courses = Course.objects.filter(tech=slug)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
#        try:
#            return Snippet.objects.filter(slug=slug)
#        except Snippet.DoesNotExist:
#            raise Http404

    def get_object(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CourseSerializer(Course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CourseSerializer(Course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CreateTechnologyView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = CourseSerializer.objects.filter(slug=slug)
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)'''


