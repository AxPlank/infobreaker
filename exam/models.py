from django.db import models
# Create your models here.

class WrittenPart(models.Model):
    part = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Problem(models.Model):
    type = models.CharField(max_length=255)
    type_integer = models.IntegerField()
    part = models.IntegerField()
    question = models.TextField()
    example = models.ImageField(null=True, blank=True, upload_to=f'media/problem/{type}/{part}/')
    ex1 = models.TextField(null=True, blank=True)
    ex2 = models.TextField(blank=True, null=True)
    ex3 = models.TextField(blank=True, null=True)
    ex4 = models.TextField(blank=True, null=True)
    answer = models.CharField(null=True, blank=True, max_length=255)
    comment = models.TextField()

    def __str__(self):
        title = f'{self.type} part {self.part}. {self.question}'
        return title

class PracticalPart(models.Model):
    part = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name