from .models import user
from .serializer import UserSerializer,UserModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
# Create your views here.
@api_view(["PATCH", "PUT"])
def singleobj(request, id):
    data = get_object_or_404(user,id = id)
    if request.method == "PUT":       
        parsed_data = request.data
        serializer = UserModelSerializer(data, data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update':'success'}) 
    
    if request.method == "PATCH":
        parsed_data = request.data
        serializer = UserModelSerializer(data, data = parsed_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"update":"success"})
    serializer = UserModelSerializer(data)
    return Response(serializer.data)
@api_view(["POST","GET"])
def multipleobj(request):
    if request.method == 'POST':
        parsed_data = request.data
        serializer = UserModelSerializer(data = parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response({'created':'success'},status= status.HTTP_201_CREATED )
    if request.method == "GET":
        data = user.objects.all()
        serializer = UserModelSerializer(data, many = True)
        return Response(serializer.data)
class MultipleobjAPIView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = user.objects.all()
    serializer_class = UserModelSerializer
    def get(self, request, *args, **kwargs):
        print(request.user)
        response = super().get(request, *args, **kwargs)
        return response

class SingleObjAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = user.objects.all()
    serializer_class = UserModelSerializer
    








    