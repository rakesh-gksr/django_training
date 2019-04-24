from datetime import datetime
from django.utils import timezone
from mercury.models import UserToken

token_expiration_duration_min = 90*24*60 #90 days
user_token_exiration_duration_min = 1*24*60 # 1 day
user_token_exiration_duration_min=1
min_to_days = 1.0/(24*60) # conversion factor

def now():
    return timezone.now()

def get_expiry(created, max_duration_min):

    diff  = timezone.now() - created
    diff_minutes = (diff.seconds / 60)
    return max_duration_min - diff_minutes


def get_db_items(model, filters=None):
    argument_list = dict()
    db_items = model.objects.filter()
    for keyname, value in filters.items() if filters else {}:
        argument_list.update({keyname : value})
        db_items = db_items.filter(**argument_list)
    return db_items