from django.shortcuts import HttpResponse


def homepageView(request):
    return HttpResponse('Hello, World')