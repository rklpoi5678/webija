from django import template
from django.utils import timezone
import datetime

register = template.Library()

@register.filter(name='custom_date')
def custom_date(value):
    now = timezone.now()
    delta = now - value

    if delta < datetime.timedelta(days=1):
        return f'{delta.seconds // 3600}시간 전'
    elif delta < datetime.timedelta(days=365):
        return value.strftime('%m-%d 에 작성됨')
    else:
        return value.strftime('%Y-%m')
