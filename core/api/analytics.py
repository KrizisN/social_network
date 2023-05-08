from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.manager import posts as manager_posts


@api_view(['GET'])
def analytics(request):
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if not date_from or not date_to:
        return Response({'detail': 'Date_from and date_to parameters must be specified.'}, status=status.HTTP_400_BAD_REQUEST)

    likes = manager_posts.get_likes_by_date_range(date_from, date_to)

    return Response(likes)
