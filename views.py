from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from Cyber_Users.models import UserAdd_Model


def AdminLogin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'admin' and password == 'admin':
            return redirect('UserDetails')
    return render(request, 'admins/AdminLogin.html')


def Analysis(request):
    chart = UserAdd_Model.objects.values(
        'attackresult', 'method').annotate(dcount=Count('attackresult'))
    return render(request, 'admins/Analysis.html', {'objects': chart})


def UserDetails(request):
    obj = UserAdd_Model.objects.all()
    return render(request, 'admins/UserDetails.html', {'object': obj})
