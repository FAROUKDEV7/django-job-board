from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE=[
    ('part time','part time'),
    ('full time','full time'),
]



class Job(models.Model):
    user=models.ForeignKey( User ,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    # location
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    Published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='jobphoto/%y/%m/%d')
    slug=models.SlugField(null=True,blank=True)




    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
    

class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    website=models.URLField(max_length=100)
    cv=models.FileField(upload_to='applyjob/')
    coverletter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    