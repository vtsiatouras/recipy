from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter


class OptionalSlashRouter(DefaultRouter):
    """Router to make trailing slashes optional. All URLs work with or without trailing slashes, without redirecting.
    """
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


router = OptionalSlashRouter()

urlpatterns = [
    url(r'^', include(router.urls))
]
