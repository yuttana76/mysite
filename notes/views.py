# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note

# Create your views here.
def home(request):
    notes = Note.objects
    template = loader.get_template('note.html')
    context = {'notes': notes}
    return render(request, 'note.html', context)
    #return render_to_response("note.html", notes)