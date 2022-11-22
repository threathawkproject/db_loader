from django.urls import path
from .views import (
    IocViewSet,
    SourceIocViewSet,
    DateIocViewSet,
    IocTypeViewSet
)

urlpatterns = [
    path("ioc_feeds_consumer", IocViewSet.as_view({
        "get": "list"
    })),
    path('ioc_feeds_consumer/sources/<str:source>/', SourceIocViewSet.as_view({
        "get": "get"
    })),
    path('ioc_feeds_consumer/date', DateIocViewSet.as_view({
        "get": "get"
    })),
    path('ioc_feeds_consumer/ioc_type/<str:ioc_type>/', IocTypeViewSet.as_view({
        "get": "get"
    })),
]
