from rest_framework import routers
from action.views import ActionSeriesViewSet, ActionViewSet

router = routers.DefaultRouter()

router.register(r'action_series', ActionSeriesViewSet)
router.register(r'action', ActionViewSet, base_name='action')
