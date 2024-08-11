from django.db import models

# Create your models here.

JOB_TYPE=[
    ('part time','part time'),
    ('full time','full time'),
]



class Job(models.Model):
    title=models.CharField(max_length=100)
    # location
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    Published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    def __str__(self):
        return self.title
    
