from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length = 80, unique = True)
    course_number = models.PositiveSmallIntegerField(unique = True, primary_key = True)
    course_term = models.CharField(max_length = 6)
    course_year = models.PositiveSmallIntegerField()
    course_grade = models.DecimalField(blank = True, null = True, max_digits = 5, decimal_places = 2)

class Assignment_Weight(models.Model):
    course_number = models.ForeignKey(Course, on_delete = models.CASCADE)
    assignment_type = models.CharField(max_length = 50)
    assignment_weight = models.DecimalField(max_digits = 3, decimal_places = 3)

class Assignment_Grade(models.Model):
    course_number = models.ForeignKey(Course, on_delete = models.CASCADE)
    assignment_type = models.ForeignKey(Assignment_Weight, on_delete = models.CASCADE)
    assignment_grade = models.DecimalField(max_digits = 5, decimal_places = 2)

