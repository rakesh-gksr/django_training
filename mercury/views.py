from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import formats

from . import utils
from mercury.models import UserToken

@api_view(['GET'])
def user_token(request):
    """
    List all code snippets, or create a new snippet.
    """
    result = None
    token = UserToken.objects.filter(user_id='vipul.jain12@db.com')
    for token in token:
        result = {
            "created": formats.date_format(token.created, 'd-m-Y H:i:s'),
            "user_id": token.user_id,
            "token": token.token,
            'expire': int(utils.get_expiry(token.created, utils.user_token_exiration_duration_min))
        }

    return Response(result)