from django.utils import timezone
from users.models import User


class UserLastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user and request.user.is_authenticated:
            user = User.objects.get(pk=request.user.pk)
            user.last_request = timezone.now()
            user.save()

        response = self.get_response(request)

        return response
