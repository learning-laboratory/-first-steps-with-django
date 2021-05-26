from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse(f"<h1>Hello World!</h1>{request.user}")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    context = {
        'text': 'this is about us',
        'number': 123,
        'list': [11,22,33,44,55, "abc"],
        'text_html': '<h1>Hello Word!</h1>'
    }
    return render(request, "about.html", context)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})