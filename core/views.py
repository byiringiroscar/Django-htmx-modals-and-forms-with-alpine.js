from django.shortcuts import render
from core.forms import ComplaintForm
from core.models import Complaint

# Create your views here.


def index(request):
    form = ComplaintForm()
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'partials/success.html')
        return render(request, 'partials/failure.html')
    form = ComplaintForm()
    context = {
        "form": form,
    }
    return render(request, "index.html", context)