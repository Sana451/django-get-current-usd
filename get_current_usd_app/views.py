from datetime import datetime, timezone

from django.http import JsonResponse
from get_current_usd_app.usd_api.get_current_usd_from_api import get_current_usd_from_api
from get_current_usd_app.models import Rate


def get_current_usd(request):

    if (datetime.now(timezone.utc) - Rate.objects.first().request_datetime).seconds < 10:
        return JsonResponse(data={"Try later": "You can do only 1 request per 10 second"})

    result_data = dict()

    rate = get_current_usd_from_api()

    Rate.objects.create(rate=rate, request_datetime=datetime.now(timezone.utc))
    last_10_requests = [(r.rate, r.request_datetime) for r in Rate.objects.all()[:10]]

    result_data["current_conversion_rate_usd_to_rub"] = rate
    result_data["last_10_rate_usd_to_rub_requests"] = last_10_requests

    return JsonResponse(data=result_data)
