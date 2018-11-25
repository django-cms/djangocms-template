from .views import *

# Rest Framework
from rest_framework import routers

router = routers.SimpleRouter()
# order matters!

router.register(r'hubspot/check-email', HubspotContactByEmailViewSet, base_name='hubspot_check_email')
