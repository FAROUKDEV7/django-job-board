from django import forms
from .models import Apply
from .models import Job 
class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','website','cv','coverletter']


class PostForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('user','slug')
   
        