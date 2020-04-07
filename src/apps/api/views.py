from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import ApplicationSerializer
from .models import Application


class ApplicationViewSet(ModelViewSet):
    lookup_field = 'api_key'
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def list(self, request, *args, **kwargs):
        raise Http404()

    @action(detail=False, methods=['GET'], name='Get Highlight')
    def generate_api_key(self, request, *args, **kwargs):
        api_key = request.query_params.get('api_key')
        try:
            app: Application = get_object_or_404(Application, api_key=api_key)
        except ValidationError:
            raise Http404()

        app.generate_api_key()
        app.save()
        serializer = self.get_serializer(app)

        return Response(serializer.data)
