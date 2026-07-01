from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm



@login_required
# def home(request):
#     return HttpResponse('<h1> Welcome to TicTacarena<h1><br><a href="/logout/">Logout</a>')


@login_required
def lobby(request):
    return render(request,"users/lobby.html")

def register_view(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user  = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    

    return render(request,"users/register.html",{"form":form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                next_url = request.POST.get("next") or "lobby"
                return redirect(next_url)

    
    else:
        form=LoginForm()

    
    return render(request,"users/login.html",{"form":form})


def logout_view(request):
    logout(request)
    return redirect("login")



