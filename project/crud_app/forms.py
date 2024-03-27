from django import forms
from .models import VotingCard

class VotingCardForm(forms.ModelForm):
    class Meta:
        model = VotingCard
        fields = "__all__"

        labels = {
            'dob' : 'Date Of Birth'
        }

        widgets = {
            'firstname' : forms.TextInput(attrs={'class':'form-control'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'address' : forms.Textarea(attrs={'rows':5,'class':'form-control'}),
            'constituency' : forms.TextInput(attrs={'class':'form-control'})
        }
