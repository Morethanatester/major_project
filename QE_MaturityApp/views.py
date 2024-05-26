from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, QE Maturity App!")