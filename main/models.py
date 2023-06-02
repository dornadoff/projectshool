from django.db import models

class Clas(models.Model):
    character = models.CharField(max_length=1)
    number = models.SmallIntegerField()
    def __str__(self):
        return f"{self.number}-{self.character}"

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_bearth = models.DateField()
    clas = models.OneToOneField(Clas, on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_bearch = models.DateField(null=True, blank=True)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="icon/", default="default.png")
    def __str__(self):
        return self.full_name

class Picture(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images/")
    students = models.ManyToManyField(Student)
    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    telegram = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.full_name
