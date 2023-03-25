from django.urls import path
from django.http import HttpResponse
from django.template import loader

from .views import IndexPageView

def show_phones(request):
    template = loader.get_template('base.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


urlpatterns = [
    path('menu/', IndexPageView.as_view(), name='index'),
    path('', show_phones),
]