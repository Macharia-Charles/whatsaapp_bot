from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'AC62738410402f5ee4cc49b31d4c596e2b'
auth_token = '4f13964fc131515a644951c9036ab0c3'
client = Client(account_sid, auth_token)


@csrf_exempt
def bot(request):
    message = request.POST["Body"]
    SenderName = request.POST["ProfileName"]
    SenderNum = request.POST['From']
    if message == "hi" or "hello" or "Hi" or "Hello":
        client.messages.create(
            body="Hi {}, How's the going?".format(SenderName),
            from_='whatsapp:+14155238886',
            to=SenderNum)
        client.messages.create(
            body="How may we be of help to you {}?".format(SenderName),
            from_='whatsapp:+14155238886',
            to=SenderNum)
    return HttpResponse('hello')
