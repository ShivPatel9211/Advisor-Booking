from django.shortcuts import render
from rest_framework.views import APIView
from . serialiazer import AdvisorSerializers ,UserSerializers
from .models import Advisor,Booking
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from django.contrib.auth import authenticate
# Create your views here.
class addAdvisor(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes=(IsAuthenticated,)
    def post(self,request):
        serializer = AdvisorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class userRegister(APIView):
    def post(self, request):
        serializer =UserSerializers(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({"userId":serializer.data['id'],'Token': str(refresh.access_token),},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class userLogin(APIView):
    def post(self,request):
        data=request.data
        email=data.get('email','')
        password=data.get('password','')
        print("this is ",email)
        if email=="":
            return Response({"Error":"Email can't be blank"},status=status.HTTP_400_BAD_REQUEST)
        if password=="":
            return Response({"Error":"Password can't be blank"},status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(email=email,password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'User Id':user.id ,'Token': str(refresh.access_token)},status=status.HTTP_200_OK)
        return Response({"Error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)

class getAdvisor(APIView):
    def get(self,request,userId):
        User=get_user_model()
        try:
            user= User.objects.get(id=userId)
            if user is not None:
                advisor= Advisor.objects.all()
                serializer = AdvisorSerializers(advisor, many=True)
                return Response({"Advisor":serializer.data},status=status.HTTP_200_OK)
        except:
            return Response({"Error":"User not exist"},status=status.HTTP_400_BAD_REQUEST)

class bookAdvisor(APIView):
    def post(self,request,userId,advisorId):
        User=get_user_model()
        user=User.objects.get(id=userId)
        advisor=Advisor.objects.get(id=advisorId)
        book = Booking(user=user,advisor=advisor)
        book.save()
        return Response(status=status.HTTP_200_OK)


class getBooking(APIView):
    def get(self,request,userId):
        booked=Booking.objects.filter(user=userId)
        if len(booked)!=0:
            data=[]
            for i in booked:
                bookedTime=i.booking_time
                bookedTimeF=f"{bookedTime.year}/{bookedTime.month}/{bookedTime.day} {bookedTime.hour}:{bookedTime.minute}"
                data.append(
                    {"Booking Id":i.id,"Advisor Name":i.advisor.name,"Advisor Profile Pic":i.advisor.profile_pic.url,"Booking Time":bookedTimeF}
                )
            return Response({"Booking":data},status=status.HTTP_200_OK)
        return Response({"Sorry, No booking found."},status=status.HTTP_404_NOT_FOUND)


