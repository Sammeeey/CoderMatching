from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.template import context
from django.urls import reverse
from django.views.generic.detail import DetailView

from .forms import CreateAdForm
from .models import Ad, Comment

from django.utils import timezone

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world, You're at the codermatch index (main page). Here you should be able to see a collection of the most recent (or popular, or ...) ads. Maybe you could also be able to search ads from here with a search text field.")

    # latestAdList = Ad.objects.order_by('-pubDate')[:6]
    # output = ', '.join([ad.projectTitle for ad in latestAdList])
    # return HttpResponse(output)

    # latestAdLi = Ad.objects.order_by('-pubDate')[:6]
    # template = loader.get_template('codermatch/index.html')
    # context = {
    #     'latestAdList': latestAdLi,
    # }
    # return HttpResponse(template.render(context, request))
    
    latestAdLi = Ad.objects.order_by('-pubDate')[:5]
    context = {'latestAdList': latestAdLi}
    return render(request, 'codermatch/index.html', context) #render is the shortcut to taking a request, loading a template and respond the HTML text result based on the context dictionary


class AdDetailView(DetailView):
    model = Ad
    template_name = 'codermatch/detail.html'

def createAd(request):
    """
    This view method enables to publish own individual ads on the page.
    """
    # if POST request: process form data
    if request.method == 'POST':
        # create form instance + populate it with request data
        form = CreateAdForm(request.POST)
        # check if it's valid
        if form.is_valid():
            # process form.cleaned_data as required
            newAd = form.save()
            # redirect to new URL:
            return HttpResponseRedirect(reverse(viewname='codermatch:adDetail', args=(newAd.id,)))
    # if it's a GET request: show the unpopulated form
    elif request.method == 'GET':
        form = CreateAdForm()
    # if it's neither a POST, nor a GET request: send back to index page
    else:
        raise Http404('Only GET and POST requests are allowed')
    
    return render(request=request, template_name='codermatch/createAd.html', context={'form': form})


def contribute(request):
    return render(request, template_name='codermatch/contribute.html')


def adSearch(request):
    return HttpResponse('This function should should view a search where people could sort and search for ads with certain properties...')






def testTemplating(request, numArg=10):
    vari = 'a Python string'
    numi = 89.3
    context = {'numArg': numArg, 'vari': vari, 'numi': numi}
    return render(request, 'codermatch/testTemplating.html', context=context)