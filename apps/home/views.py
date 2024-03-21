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
        load_template = request.path.split('/')[-1]
        print("load_template", load_template)
        context['segment'] = load_template
        print(context)
        html_template = loader.get_template('home/' + load_template)
        print(1)
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        print(1)
        print(context['segment'], "rawdata.html")
        if context['segment'] == "rawdata.html":
            print("success")
            data = RawData.objects.all
            context_1 = {
                'data': data
            }
            return render(request, "home/rawdata.html", context_1)
        
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
