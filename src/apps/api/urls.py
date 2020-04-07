from django.urls import path
from rest_framework import routers
from .views import ApplicationViewSet


app_name = 'api'


router = routers.SimpleRouter()
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('test/<str:api_key>/', ApplicationViewSet.as_view({'put': 'retrieve'}))
] + router.urls
