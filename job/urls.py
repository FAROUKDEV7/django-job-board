from django.urls import path
from . import views
from . import api
app_name='job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add,name='add'),
    path('<str:slug>',views.job_detail,name='job_detail'),

    # rest framework , api
    path('api/list',api.joblistapi,name='joblistapi')
]
