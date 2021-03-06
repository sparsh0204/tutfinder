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
    CourseListSerializer,
    CourseDetailSerializer,
    CourseCreateUpdateSerializer,
    CourseDeleteSerializer,
    SubmitCourseCreateUpdateSerializer,
)

from .models import Course, SubmitCourse

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

class SubmitCourseCreateAPIView(CreateAPIView):
    queryset = SubmitCourse.objects.all()
    serializer_class = SubmitCourseCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)