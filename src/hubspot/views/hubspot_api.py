from django.conf import settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
import requests
from ..serializers import EmailSerializer
from rest_framework import viewsets, permissions, mixins, status



class HubspotContactByEmailViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Check whether a contact exists in the hubspot database
    """

    renderer_classes = [
        # the only order in which csv headers work and the browsable api returns pretty json
        JSONRenderer,
        BrowsableAPIRenderer,
    ]

    authentication_classes = []

    # DRY Permissions dont apply here as this is not a Model View Set, but a custom one.
    permission_classes = (
        permissions.AllowAny,
    )

    serializer_class = EmailSerializer

    # its better to use the ViewSet instead of views.API: https://www.stackoverflow.com/questions/30389248

    def create(self, request, *args, **kwargs):
        """
        Return the info as a list of dicts
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')

        params = {
            'hapikey': settings.HUBSPOT_API_SECRET,
        }

        headers = {
            'Content-Type': 'application/json',
        }
        data = requests.get(
            'https://api.hubapi.com/contacts/v1/contact/email/{}/profile?='.format(
                email,
            ),
            params=params,
            headers=headers,
        )

        response = data.json()

        # status is set to 'error' if there is no matching email address
        if response.get('status', None):
            # do not send 404! https://code.djangoproject.com/ticket/17734
            return Response({'status': 'error'})

        return Response({'status': 'success'})
