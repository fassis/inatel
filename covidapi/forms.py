from django import forms

class StateForm(forms.Form):
    state = forms.CharField(label='Estado', max_length=32)