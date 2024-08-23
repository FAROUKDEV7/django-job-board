from .serializers import JobSerializers
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view


# api

@api_view(['GET'])
def joblistapi(request):
    all_job=Job.objects.all()
    data=JobSerializers(all_job , many=True).data
    return Response({'data':data})