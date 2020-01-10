from django.shortcuts import render, redirect


def rd_view(request):
    print(request.user)
    if request.user.__str__() == 'AnonymousUser':
        return redirect('job_view:login')
    return redirect('job_view:main')


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')


def jobs_analyse(request):
    return render(request, 'jobs_analyse.html')

