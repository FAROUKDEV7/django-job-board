from django.urls import path
from . import views
from . import api
app_name='job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add,name='add'),
    path('<str:slug>',views.job_detail,name='job_detail'),

    # function based view, api 
    path('api/jobs',api.job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),


    # class , api
    path('api/jobs/add',api.AddJobListApi.as_view(),name='AddJobListApi'),
    path('api/jobs/edit/<int:id>',api.JobEditApi.as_view(),name='JobEditApi'),
]
