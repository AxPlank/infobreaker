from django.db import models
# Create your models here.

class WrittenPart(models.Model):
    part = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Problem(models.Model):
    type_integer = models.IntegerField()
    part = models.IntegerField()
    question = models.TextField()
    example = models.ImageField(null=True, blank=True, upload_to=f'problem/{type_integer}/{part}/{question}')
    ex1 = models.TextField(null=True, blank=True)
    ex2 = models.TextField(blank=True, null=True)
    ex3 = models.TextField(blank=True, null=True)
    ex4 = models.TextField(blank=True, null=True)
    answer = models.CharField(null=True, blank=True, max_length=255)
    comment = models.TextField()
    comment_img = models.ImageField(null=True, blank=True, upload_to=f'problem/{type_integer}/{part}/{question}')

    def __str__(self):
        if self.type_integer == 1:
            title = f'필기 part {self.part}. {self.question}'
            return title
        else:
            title = f'실기 part {self.part}. {self.question}'
            return title

class PracticalPart(models.Model):
    part = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name