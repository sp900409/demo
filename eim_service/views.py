import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from eim_service.models import UnitInfo


def status_list(request):
    output = UnitInfo.objects.order_by('unit_no')

    # return HttpResponse(output)
    return render(request, 'status_list.html',{'Units': output})
