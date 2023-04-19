from operator import index
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import RegistrationForm


#my imports.................
from .models import ArmoryData,heronWicks,Mission
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    armrydata=ArmoryData.objects.all()
    heron=heronWicks.objects.all()
    data={'armrydata':armrydata,'heron':heron}
    return render(request,'index.html',data)



def register(request):
       if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=form.save()
            user = authenticate(request, username=username, password=password) # for login 
            
            #this line makes the error - bcz login authenticn not working nd also ther is no need to use..
            
            # login(request,user) 
            
            #messages.success(request, f'Account created for {username}!')
            return redirect('usr_login')# redirecting to login func for users
       else:
        form = RegistrationForm()
       return render(request, 'registration.html', {'form': form})










def usr_login(request):
    if request.method =='POST':
        # error and page does not go to another pg bcz we did nt use 'request,' before reqt.post, very imp reqst all things
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) # not matter this login()
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})


def feedback(request):
    return render(request,'feedback.html')



def checkoutbuy(request):
    return render(request,'checkoutbuy.html')



def registration(request):
    return render(request,'registration.html')    


def mission1(request):
    mis1 = Mission.objects.all()
    
    mis_data = {'mis1': mis1}
    return render(request,'mission1.html', mis_data)



def confirmation(request):
    return render(request,'confirmation.html')



 