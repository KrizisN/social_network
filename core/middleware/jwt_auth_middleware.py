from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_auth_tuple = JWTAuthentication().authenticate(request)
        if user_auth_tuple is not None:
            request.user, request.auth = user_auth_tuple

        response = self.get_response(request)
        return response
