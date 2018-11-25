
from django.conf.urls import url, include
from api import routers
from what_capital.urls import router as what_capital_router
from usermgmt.api.urls import router as usermgmt_router

# Rest Framework
router = routers.DefaultRouter()
router.extend(usermgmt_router)
router.extend(what_capital_router)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
