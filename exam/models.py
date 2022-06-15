from django.db import models
# Create your models here.

class WrittenPart(models.Model):
    part = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WrittenQuestion(models.Model):
    part = models.IntegerField()
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='written/5/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    answer = models.IntegerField()
    comment = models.TextField()

class PracticalPart(models.Model):
    part = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PracticalQuestion(models.Model):
    part = models.IntegerField()
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/1/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()