import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import MyUser, Course, Enrollment, Assignment, Submission, Grade, Notification
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Generate dummy data for the database'

    def handle(self, *args, **kwargs):
        first_names = ['Ali', 'Sara', 'Reza', 'Mina', 'Hassan', 'Ladan']
        last_names = ['Ahmadi', 'Hosseini', 'Karimi', 'Farhadi', 'Rahimi']
        course_titles = ['Python Basics', 'Advanced Django', 'REST API Mastery', 'Data Science 101']
        assignment_titles = ['Assignment 1', 'Midterm Project', 'Final Report', 'Extra Credit']

        # Create teachers
        teachers = []
        for _ in range(3):
            first = random.choice(first_names)
            last = random.choice(last_names)
            teacher = MyUser.objects.create_user(
                username=f'{first.lower()}{last.lower()}{random.randint(100,999)}',
                first_name=first,
                last_name=last,
                email=f'{first.lower()}.{last.lower()}@school.com',
                password='password123',
                role='teacher'
            )
            teachers.append(teacher)

        # Create students
        students = []
        for _ in range(10):
            first = random.choice(first_names)
            last = random.choice(last_names)
            student = MyUser.objects.create_user(
                username=f'{first.lower()}{last.lower()}{random.randint(100,999)}',
                first_name=first,
                last_name=last,
                email=f'{first.lower()}.{last.lower()}@student.com',
                password='password123',
                role='student'
            )
            students.append(student)

        # Create courses
        courses = []
        for title in course_titles:
            course = Course.objects.create(
                title=title,
                description=f"This is a course about {title}.",
                teacher=random.choice(teachers)
            )
            courses.append(course)

        # Enroll students randomly
        for student in students:
            selected_courses = random.sample(courses, k=random.randint(1, 3))
            for course in selected_courses:
                Enrollment.objects.get_or_create(student=student, course=course)

        # Create assignments
        assignments = []
        for course in courses:
            for title in assignment_titles:
                assignment = Assignment.objects.create(
                    course=course,
                    title=title,
                    description=f"{title} description",
                    due_date=timezone.now() + timezone.timedelta(days=random.randint(3, 30))
                )
                assignments.append(assignment)

        # Create submissions and grades
        for assignment in assignments:
            for enrollment in Enrollment.objects.filter(course=assignment.course):
                student = enrollment.student
                # Create submission
                submission = Submission.objects.create(
                    assignment=assignment,
                    student=student,
                    file=ContentFile(b"dummy file content", name="submission.txt")
                )
                # Grade it
                Grade.objects.create(
                    submission=submission,
                    score=random.uniform(60, 100),
                    feedback="Good job!"
                )

        # Create notifications
        for student in students:
            for _ in range(3):
                Notification.objects.create(
                    user=student,
                    message=f"Hello {student.first_name}, check your grades!",
                )

        self.stdout.write(self.style.SUCCESS("Dummy data created successfully."))
