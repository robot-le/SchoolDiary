from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True)

    # pair = models.ManyToManyField(
    #     'self',
    #     null=True,
    #     # on_delete=models.SET_NULL,
    #     symmetrical=True,
    # )

    mentor = models.ForeignKey(
        'self',
        related_name='mentee',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(
        Student,
        through='Grade'
    )

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='groups')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='groups')
    grade = models.IntegerField(null=True)
