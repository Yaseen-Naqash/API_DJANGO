from django.contrib import admin
from django.contrib import admin
from .models import Course, Enrollment, Assignment, Submission, Grade, Notification, MyUser
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher", "created_at")
    list_filter = ("teacher",)
    search_fields = ("title",)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "enrolled_at")
    list_filter = ("course",)
    search_fields = ("student__username", "course__title")

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "due_date", "created_at")
    list_filter = ("course",)
    search_fields = ("title",)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("assignment", "student", "submitted_at")
    list_filter = ("assignment",'assignment__course')
    search_fields = ("student__username",)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    

    readonly_fields = ('course',)

    list_display = ("submission", "score")
    search_fields = ("submission__student__username",)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "is_read", "created_at")
    list_filter = ("is_read",)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")