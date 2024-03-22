# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import RawData
from django.shortcuts import render



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        print("Click Once")
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        print(load_template)
        
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        if load_template == "rawdata.html":
            all_data = RawData.objects.all
            context['all_data'] = all_data
            
            html_template = loader.get_template('home/' + load_template)
            return HttpResponse(html_template.render(context, request))
        
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
