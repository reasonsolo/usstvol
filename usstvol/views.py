# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.template import RequestContext

from models import Applicant, Event
from forms import ApplicantForm

def home(request):
  return redirect(reverse('usstvol.views.apply'))
  pass


@csrf_protect
def apply(request):
  form = ApplicantForm()
  success = False
  if request.method == 'POST':
    form = ApplicantForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      success = True
    pass

  return render_to_response('apply.html', {
    'form': form,
    'success': success,
    }, context_instance = RequestContext(request))

