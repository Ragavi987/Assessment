"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm
from .models import *

class ApplyForm(ModelForm):
    class Meta:
        model = Candidates
        fields = "__all__"

