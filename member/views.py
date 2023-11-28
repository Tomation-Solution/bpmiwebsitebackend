from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from . import models
from rest_framework.response import Response
from rest_framework import status
class BecomeMemberSerializer(serializers.ModelSerializer):
    certifications = serializers.ListField(child=serializers.FileField())
    class Meta:
        model = models.BecomeAMember
        fields ='__all__'


    def create(self, validated_data):
        cert = validated_data.pop('certifications')
        member = models.BecomeAMember.objects.create(**validated_data)
        for eachCert in  cert:
            models.BecomeAMemberFiles.objects.create(member=member,file= eachCert)

        return member
    

@api_view(['POST'])
@permission_classes([AllowAny])
def register_become_a_member(request,*args,**kwargs):
    serailzer = BecomeMemberSerializer(data=request.data)
    serailzer.is_valid(raise_exception=True)
    serailzer.save()
    return Response(status=status.HTTP_201_CREATED,data={'message':'Submitted Successfully'})