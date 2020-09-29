from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
import random
import string
from .models import ShortendURL

def index(request):
    url_items = ShortendURL.objects.all()
    context = {
        'url_items': url_items,
    }
    return render(request, 'UrlShort/index.html', context)

def save(request):
    input_url = request.POST['input_url']
    def createCode():
        output_code = []
        for i in range(10):
            output_code += random.choice([random.choice(string.ascii_letters), random.choice(string.digits)])
        output_code = ''.join(output_code)
        return output_code

    output_code = createCode()
    while ShortendURL.objects.filter(code=output_code).exists():
        output_code = createCode

    url_item = ShortendURL(code=output_code, url=input_url)
    url_item.save()

    return HttpResponseRedirect(reverse('urlshort:index'))

def delete(request, url_item_id):
    url_item = ShortendURL.objects.get(id=url_item_id)
    url_item.delete()
    return HttpResponseRedirect(reverse('urlshort:index'))

def redirect_view(request, input_code):
    url_item = ShortendURL.objects.get(code=input_code)
    return redirect(url_item.url)