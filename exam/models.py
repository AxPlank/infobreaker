from django.db import models
from rest_framework import serializers
# Create your models here.

class WrittenPart1(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='written/1/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    comment = models.CharField()

class WrittenPart2(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='written/2/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    comment = models.CharField()

class WrittenPart3(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='written/3/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    comment = models.CharField()

class WrittenPart4(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='written/4/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    comment = models.CharField()

class WrittenPart5(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='written/5/')
    ex1 = models.TextField()
    ex2 = models.TextField()
    ex3 = models.TextField()
    ex4 = models.TextField()
    comment = models.CharField()

class PracticalPart1(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/1/')
    comment = models.CharField()

class PracticalPart2(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/2/')
    comment = models.CharField()

class PracticalPart3(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/3/')
    comment = models.CharField()

class PracticalPart4(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/4/')
    comment = models.CharField()

class PracticalPart5(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/5/')
    comment = models.CharField()

class PracticalPart6(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/6/')
    comment = models.CharField()

class PracticalPart7(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/7/')
    comment = models.CharField()

class PracticalPart8(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/8/')
    comment = models.CharField()

class PracticalPart9(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/9/')
    comment = models.CharField()

class PracticalPart10(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/10/')
    comment = models.CharField()

class PracticalPart11(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/11/')
    comment = models.CharField()

class PracticalPart12(models.Model):
    question = models.CharField()
    example = models.ImageField(blank=True, upload_to='practice/12/')
    comment = models.CharField()
