from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    if request.method =='POST':
        if request.POST['passwd'] == request.POST['passwdconfirm']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'username has already been alredy taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['passwd'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method =='POST':
        usrname = request.POST['username']
        pw = request.POST['passwd']
        user = authenticate(username = usrname, password=pw)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username and password doesn\'t match'})
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')