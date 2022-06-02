from django.http import HttpResponse
from hadith.services import get_random_hadith, send_whatsapp_message
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def receive_message(request):
    request_body = request.POST
    from_ = request_body.get("From")
    to = request_body.get("To")
    hadith = get_random_hadith()
    send_whatsapp_message(from_=to, to=from_, body=hadith)
    return HttpResponse()


@csrf_exempt
def message_status(request):
    return HttpResponse()
