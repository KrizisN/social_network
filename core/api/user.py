from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def user_activity(request):
    user = request.user
    last_login = user.last_login
    last_request = user.last_request

    return Response({
        'last_login': last_login,
        'last_request': last_request
    })
