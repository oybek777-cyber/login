from django.shortcuts import render,redirect
from .forms import CustomUSerCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        form=CustomUSerCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,'tizimdan otigiz')

            return redirect('login')            
    else:
        form=CustomUSerCreationForm()

        context={
            'form':form
        }
        return render(request=request,template_name='register.html',context=context)    