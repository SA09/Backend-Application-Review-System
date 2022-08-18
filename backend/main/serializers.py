from telnetlib import STATUS
from rest_framework import serializers
from .models import Candidate
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields=('id','full_name','email','contact','address','status')