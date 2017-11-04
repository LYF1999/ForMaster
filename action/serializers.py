#  coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from action.models import ActionSeries, Action

from config.settings import MEDIA_ROOT
from os import path
import os


def handle_uploaded_file(path, f):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class ActionSerializer(serializers.ModelSerializer):
    series_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Action
        fields = ['video', 'series_id']

    def create(self, validated_data):
        series_id = validated_data['series_id']
        series = get_object_or_404(ActionSeries, id=series_id)
        folder_name = '{}_{}'.format(series.id, series.name)
        folder_path = path.join(MEDIA_ROOT, folder_name)

        if not path.isdir(folder_path):
            os.mkdir(folder_path)

        file_path = path.join(folder_path, validated_data['video'].name)
        file_url = '{}/{}'.format(folder_name, validated_data['video'].name)

        handle_uploaded_file(file_path, validated_data['video'])
        return Action.objects.create(series=series, video=file_url)


class ActionSeriesSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(source='action_set.all', many=True, read_only=True)

    class Meta:
        model = ActionSeries
        fields = ['id', 'name', 'desc', 'actions']
