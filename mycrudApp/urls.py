# from django.urls import include, path
# from rest_framework import routers
# from . import views
#
# router = routers.DefaultRouter()
# router.register(r'driver', views.DriverViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


from django.urls import path
from .views import DriverView

app_name = 'mycrudApp'
urlpatterns = [
    path('driver/', DriverView.as_view()),
    path('driver/<int:pk>', DriverView.as_view())
]