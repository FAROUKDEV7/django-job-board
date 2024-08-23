from .serializers import JobSerializers
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

# api


# get all job
@api_view(['GET'])
def job_list_api(request):
    all_job=Job.objects.all()
    data=JobSerializers(all_job , many=True).data
    return Response({'data':data})



# get one job
@api_view(['GET'])
def job_detail_api(request,id):
    job_detail=Job.objects.get(id=id)
    data=JobSerializers(job_detail).data
    return Response({'data':data})



# class based views


class AddJobListApi(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializers



class JobEditApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializers
    lookup_field='id'

    