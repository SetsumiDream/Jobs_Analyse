from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')


def jobs_analyse(request):
    return render(request, 'jobs_analyse.html')