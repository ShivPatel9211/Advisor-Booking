from rest_framework import serializers
from .models import Advisor
from django.contrib.auth import get_user_model

User=get_user_model()
class AdvisorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Advisor
        fields=['id','name','profile_pic']

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','name','password','email']
        # extra_kwargs = {'email': {'required': True}}
    def create(self, validated_data):
        user= User.objects.create(name=validated_data['name'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
