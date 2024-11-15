from django.shortcuts import render,redirect
from user.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required

def signup(request):
    if(request.method=='POST'):
       user=UserRegisterForm(request.POST)
       if(user.is_valid()):
           user.save()
           username = user.cleaned_data.get('username')
           messages.success(request, f'Account created for {username}!')
           return redirect('/user/login')

    else:
        user = UserRegisterForm()
    return render(request, 'user/signup.html', {'signup':user})

@login_required
def profile(request):
    return render(request, 'user/profile.html')



          






       
       
       


