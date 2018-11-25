from rest_framework.authentication import TokenAuthentication


class TokenAuthSupportQueryString(TokenAuthentication):
    """
    Extend the TokenAuthentication class to support querystring authentication
    in the form of "http://www.example.com/?token=<token_key>"

    needed for google spreadsheets =importcsv()
    """
    def authenticate(self, request):
        # Check if 'token_auth' is in the request query params.
        # Give precedence to 'Authorization' header.
        if 'token' in request.query_params and 'HTTP_AUTHORIZATION' not in request.META:
            return self.authenticate_credentials(request.query_params.get('token'))
        else:
            return super(TokenAuthSupportQueryString, self).authenticate(request)
