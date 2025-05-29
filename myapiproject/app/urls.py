from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, EnrollmentViewSet, AssignmentViewSet,
    SubmissionViewSet, GradeViewSet, NotificationViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]
# POST request to token endpoint with username and password key in body to get token
# GET or POST request to any endpoint with Auth key and Bearer <access token>