from django.http import HttpResponse

from .models import Question

def index(request):

    return HttpResponse("Hello, world! Now you're in polls page")