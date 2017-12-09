# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pyrebase

def login_page(request):
        return render(request, 'login.html')

