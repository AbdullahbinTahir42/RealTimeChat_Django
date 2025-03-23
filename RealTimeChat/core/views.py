from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
