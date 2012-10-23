# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import Applicant, Event
from datetime import datetime

class ApplicantForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ApplicantForm, self).__init__(*args, **kwargs)
    event_choices =  Event.objects.filter(state = 'Y')
    self.fields['event'] = forms.ModelChoiceField(label = '活动', required = True,  queryset = event_choices)

  grate_choices = [(year, year) for year in xrange(datetime.now().year - 7, datetime.now().year + 1)]
  grade = forms.ChoiceField(label = '年级', required = True, choices = grate_choices)
  class Meta:
    model = Applicant
    exclude = ('applytime')

