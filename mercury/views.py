from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from django.utils import formats

from . import utils
from mercury.models import UserToken
from mercury.schema import get_user_token_schema, delete_user_token_schema


@api_view(['GET'])
@schema(get_user_token_schema)
def get_user_token(request):
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

@api_view(['DELETE'])
@schema(delete_user_token_schema)
def delete_user_token(request, token):
    print("token==>",token)
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