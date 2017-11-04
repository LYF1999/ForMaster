#  coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from action.models import ActionSeries, Action

from config.settings import MEDIA_ROOT
from os import path
import os




class ActionSerializer(serializers.ModelSerializer):
    series_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Action
        fields = ['video', 'series_id']


class ActionSeriesSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(source='action_set.all', many=True, read_only=True)

    class Meta:
        model = ActionSeries
        fields = ['id', 'name', 'desc', 'actions']
