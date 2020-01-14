from django import forms
from .models import *


class SubsctiberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = ['']