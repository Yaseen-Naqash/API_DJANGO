from rest_framework import serializers
from .models import Course, Enrollment, Assignment, Submission, Grade, Notification, MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'role']

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'created_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']

class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'course', 'due_date', 'created_at']

class SubmissionSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    assignment = AssignmentSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'file', 'submitted_at']

class GradeSerializer(serializers.ModelSerializer):
    submission = SubmissionSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'submission', 'score', 'feedback']

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at']



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user