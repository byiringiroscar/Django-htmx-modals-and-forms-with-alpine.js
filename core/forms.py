from django import forms
from core.models import Complaint



class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ("text", "email")
        labels = {
            'text': 'Complaint',
        }



