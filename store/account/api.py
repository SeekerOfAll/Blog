from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from account.serializers import UserSerializer
from .models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @csrf_exempt
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def user_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
# #         user.delete()
# #         return HttpResponse(status=204)
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from account.serializers import UserSerializer
# from .models import User
# from rest_framework.viewsets import ModelViewSet
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # @api_view(['POST', ])
# # def registration_view(request):
# #     if request.method == 'POST':
# #         serializer = RegistrationSerializer(data=request.data)
# #         data = {}
# #         if serializer.is_valid():
# #             account = serializer.save()
# #             data['response'] = 'successful register'
# #             data['email'] = account.email
# #             data['full_name'] = account.full_name
# #         else:
# #             data = serializer.errors
# #         return Response(data)
# # @csrf_exempt
# # def user_list(request):
# #     if request.method == 'GET':
# #         users = User.objects.all()
# #         serializer = UserSerializer(users, many=True)
# #         return JsonResponse(serializer.data, safe=False)
# #     elif request.method == 'POST':
# #         data = JSONParser().parse(request)
# #         serializer = UserSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data, status=201)
# #         return JsonResponse(serializer.errors, status=400)
# #
# #
# # @csrf_exempt
# # def user_detail(request, pk):
# #     try:
# #         user = User.objects.get(pk=pk)
# #     except User.DoesNotExist:
# #         return HttpResponse(status=404)
# #
# #     if request.method == 'GET':
# #         serializer = UserSerializer(user)
# #         return JsonResponse(serializer.data)
# #
# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = UserSerializer(user, data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors, status=400)
# #
# #     elif request.method == 'DELETE':
# #         user.delete()
# #         return HttpResponse(status=204)
