from django import forms
from core.models import Complaint



class ComplaintForm(forms.ModelForm):


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.startswith('b'):
            raise forms.ValidationError("No emails beginning with 'b' allowed.")
        return email
    class Meta:
        model = Complaint
        fields = ("text", "email")
        labels = {
            'text': 'Complaint',
        }



