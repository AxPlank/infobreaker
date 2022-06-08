from django.db import models
from rest_framework import serializers
# Create your models here.

class WrittenPart1(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='written/1/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    comment = models.TextField()

class WrittenPart2(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='written/2/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    answer = models.CharField(max_length=255)
    comment = models.TextField()

class WrittenPart3(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='written/3/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    answer = models.CharField(max_length=255)
    comment = models.TextField()

class WrittenPart4(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='written/4/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    answer = models.CharField(max_length=255)
    comment = models.TextField()

class WrittenPart5(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='written/5/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    answer = models.CharField(max_length=255)
    comment = models.TextField()

class PracticalPart1(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/1/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart2(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/2/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart3(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/3/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart4(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/4/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart5(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/5/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart6(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/6/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart7(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/7/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart8(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/8/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart9(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/9/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart10(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/10/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart11(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/11/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()

class PracticalPart12(models.Model):
    question = models.TextField()
    example = models.ImageField(blank=True, upload_to='practice/12/')
    answer = models.CharField(blank=True, max_length=255)
    comment = models.TextField()
