from django.http import HttpResponse


def index(request):
    return HttpResponse("初めの言葉")
