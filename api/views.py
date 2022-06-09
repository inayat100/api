from rest_framework.views import APIView , status
from rest_framework.response import Response
from  rest_framework.decorators import api_view
from .models import registration
from .serializer import serializer_reg
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        print("#######GET______________________")
        data = registration.objects.all()
        print("data get")
        sri = serializer_reg(data,many=True)
        return Response(sri.data)
        #return Response("ok")

    if request.method == 'POST':
        print("################################")
        sri = serializer_reg(data=request.data)
        print(request.data)
        if sri.is_valid():
            sri.save()
            return Response({'msg':'saved'})
        return Response({'error':sri.errors})


# @method_decorator(csrf_exempt,name='dispatch')
# class resg(APIView):
#     def get(self,request):
#         dt = registration.objects.all()
#         seri = serializer_reg(dt,many=True)
#         return Response(seri.data)
#
#     def post(self,request):
#         # seri = serializer_reg(data=request.data)
#         # if seri.is_valid():
#         #     seri.save()
#         #     return Response({'msg':'saveed'},status=status.HTTP_201_CREATED)
#         print("####################################")
#         return Response("post")

