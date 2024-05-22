from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:index")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("myapp:index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
