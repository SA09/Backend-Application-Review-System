from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CandidateSerializer
from .models import Candidate
class CandidateViewSet(viewsets.ModelViewSet):
    queryset=Candidate.objects.all().order_by('-id')
    serializer_class=CandidateSerializer
    
