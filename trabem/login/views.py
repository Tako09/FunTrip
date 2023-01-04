from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import User
from django.views import generic
from django.utils import timezone


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'login/index.html'
    context_object_name = 'user_name'

    def get_queryset(self) -> object:
        """最新の5つの質問を表示する"""
        # Question.objects.filter(pub_date__lte=timezone.now()) は、
        # pub_date が timezone.now 以前の Question を含んだクエリセットを返します。
        return User.objects.order_by('user_name')[:5]