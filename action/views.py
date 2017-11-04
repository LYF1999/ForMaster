from rest_framework import permissions, viewsets

from action.serializers import ActionSeriesSerializer, ActionSerializer
from action.models import ActionSeries


class ActionSeriesViewSet(viewsets.ModelViewSet):
    serializer_class = ActionSeriesSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ActionSeries.objects.all()


class ActionViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ActionSerializer
    permission_classes = [permissions.AllowAny]
