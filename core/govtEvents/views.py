from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import events
from twilio.rest import Client
from django.conf import settings                                                                                                                                                      

# Create your views here.
def eventPage(request):
    eventsData = events.objects.all()
    print(eventsData)
    return render(request,'govtEvents/events.html',context={'governmentEvents':eventsData})


def addEvent(request):
    if request.method == "POST":
        event_name = request.POST['eventName']
        event_description = request.POST['eventDescription']
        event_date = request.POST['eventDate']
        event_contact = request.POST['eventContact']
        en = events(event_name=event_name,event_description=event_description,event_date=event_date,event_contact=event_contact)
        en.save()
        sendEventMessage(request)
    else:
        return HttpResponse("Method not allowed")
    return redirect("http://localhost:8000/govtEvents/eventPage/")

def sendEventMessage(request):
    latest_event = events.objects.latest('created_at')
    message_to_broadcast = (
        f"New event added: {latest_event.event_name} on {latest_event.event_date}. "
        f"Description: {latest_event.event_description} You can contact on this for more details : {latest_event.event_contact}"
    )

    client = Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN )
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return redirect("http://localhost:8000/govtEvents/eventPage/")