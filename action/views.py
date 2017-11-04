from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from action.serializers import ActionSeriesSerializer, ActionSerializer
from action.models import ActionSeries, Action

from config.settings import MEDIA_ROOT

from os import path
import os


def handle_uploaded_file(path, f):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class ActionSeriesViewSet(viewsets.ModelViewSet):
    serializer_class = ActionSeriesSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ActionSeries.objects.all()


class ActionViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ActionSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        video = request.data['file']
        series_id = request.META.get('HTTP_SID')
        series = get_object_or_404(ActionSeries, id=series_id)
        folder_name = '{}_{}'.format(series.id, series.name)
        folder_path = path.join(MEDIA_ROOT, folder_name)

        if not path.isdir(folder_path):
            os.mkdir(folder_path)

        file_path = path.join(folder_path, video.name)
        file_url = '{}/{}'.format(folder_name, video.name)

        handle_uploaded_file(file_path, video)
        return Response(ActionSerializer(Action.objects.create(series=series, video=file_url)).data, 201)

