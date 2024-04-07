from django.shortcuts import render
from core.forms import ComplaintForm
from core.models import Complaint

# Create your views here.


def index(request):
    form = ComplaintForm()
    context = {
        "form": form,
    }
    return render(request, "index.html", context)