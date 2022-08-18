from django.urls import path,include
from rest_framework import routers
from .views import CandidateViewSet
router=routers.DefaultRouter()
router.register(r'candidate', CandidateViewSet)
urlpatterns=[
    path('',include(router.urls))
]