from django.shortcuts import render, redirect
from .forms import UserCreationForm

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('authapp:login')

    context = {
        'form': form
    }

    return render(request, 'authapp/signup.html', context)