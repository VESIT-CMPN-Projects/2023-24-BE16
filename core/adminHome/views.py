import json
from django.shortcuts import render
from django.db.models import Count
from account.models import User
from complaintApp.models import Griv
from govtEvents.models import events
from govtServices.models import saveService

# Create your views here.
def adminhome(request):
    total_users = User.objects.count()
    total_events= events.objects.count()
    total_service= saveService.objects.count()
    gender_data = Griv.objects.values('gender').annotate(count=Count('id'))
    resolution_data = Griv.objects.values('preferred_resolution').annotate(count=Count('id'))
    status_data = Griv.objects.values('status').annotate(count=Count('id'))

    # Convert QuerySets to lists of dictionaries
    gender_data_list = list(gender_data)
    resolution_data_list = list(resolution_data)
    status_data_list = list(status_data)

    context = {
        'total_service':total_service,
        'total_events': total_events,
        'total_users': total_users,  # Include the total number of users in the context
        'gender_data': json.dumps(gender_data_list),
        'resolution_data': json.dumps(resolution_data_list),
        'status_data': json.dumps(status_data_list),
        'grievances': Griv.objects.all(),
    }
    return render(request,'adminHome/home.html',context)


# Create your views here.
# in views.py (sixth app)




