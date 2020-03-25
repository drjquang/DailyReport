from django.http import HttpResponse
from django.shortcuts import render
from .models import Record
from datetime import datetime


def index(request):
    records = Record.objects.all().order_by('-id')
    context = {
        "records": records,
    }
    return render(request, "records/index.html", context)
