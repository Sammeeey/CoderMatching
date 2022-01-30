from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.template import context
from django.urls import reverse

from .forms import createAdForm
from .models import Ad, Comment

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


def detail(request, adId):
    # return HttpResponse(f'You are looking at ad #{adId}')

    # try:
    #     ad = Ad.objects.get(pk=adId)
    # except Ad.DoesNotExist:
    #     raise Http404('Ad does not exist...')
    # context = {'ad': ad}
    # return render(request, 'codermatch/detail.html', context)

    ad = get_object_or_404(Ad, pk=adId) #get_object_or_404 is the shortcut to test whether an object exists and raising a Http404 response manually if it does not exist
    # context = {'ad': ad}
    # return render(request, 'codermatch/detail.html', context)

    # try to send form data as POST request on page load
    try:
        selected_comment = ad.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        # if request method is GET, render the page without an error message
        if request.method == 'GET':
            context = {
                'ad': ad,
            }
            return render(request, 'codermatch/detail.html', context=context)
        else: # if request.method == 'POST':
            # Redisplay the ad voting form.
            return render(request, 'codermatch/detail.html', {
                'ad': ad,
                'error_message': "You didn't select a comment.",
            })
    else:
        selected_comment.likes += 1
        selected_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('codermatch:adDetail', args=(ad.id,)))    


def createAd(request):
    """
    This view method enables to publish own individual ads on the page.
    """
    # if POST request: process form data
    if request.method == 'POST':
        # create form instance + populate it with request data
        form = createAdForm(request.POST)
        # check if it's valid
        if form.is_valid():
            # process form.cleaned_data as required
            newAd = Ad(projectTitle=form.cleaned_data['projectTitle'],
                        creatorName=form.cleaned_data['creatorName'],
                        projectDescription=form.cleaned_data['projectDescription'],
                        contactDetails=form.cleaned_data['contactDetails'],
                        projectStartDate=form.cleaned_data['projectStartDate'])
            newAd.save()
            # redirect to new URL:
            return HttpResponseRedirect(reverse(viewname='codermatch:adDetail', args=(newAd.id,)))
    # if it's a GET request: show the unpopulated form
    elif request.method == 'GET':
        form = createAdForm()
    # if it's neither a POST, nor a GET request: send back to index page
    else:
        raise Http404('Only GET and POST requests are allowed')
    
    return render(request=request, template_name='codermatch/createAd.html', context={'form': form})


def adSearch(request):
    return HttpResponse('This function should should view a search where people could sort and search for ads with certain properties...')






def testTemplating(request, numArg=10):
    vari = 'a Python string'
    numi = 89.3
    context = {'numArg': numArg, 'vari': vari, 'numi': numi}
    return render(request, 'codermatch/testTemplating.html', context=context)