from django.shortcuts import render, redirect
from .models import Person
from .forms import OrderForm,MsgForm
import os
from twilio.rest import Client 

# Create your views here.

def index(request):
    
    form = OrderForm()
    con_list = Person.objects.values()
    
    if request.method == 'POST' :
       
        form = OrderForm(request.POST)
        
        for list in con_list:
            if list['name'] == request.POST['name'] :
                return redirect('home')
        
        if form.is_valid():
            form.save() 

        return redirect('home')
        
    datas = Person.objects.all()
    context = { 'datas' : datas, 'form' : form }

    return render(request,'index.html' , context)

def editing(request,pk) :
    
    order = Person.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)

            if form.is_valid():
                form.save()

            return redirect('home')
    
    datas = Person.objects.all()
    context = { 'datas' : datas,'form' : form }        
    
    return render(request,'index.html' , context)

def msg(request,pk) :
    
    form = MsgForm()
    data = Person.objects.get(id=pk)
    
    if request.method == 'POST' :
                
        form  = MsgForm(request.POST)
        msg_ = request.POST['msg']
        
        form.save()
        
        SID = 'ACc52cdc026ba39d5bd793d6823daaf513'
        AUTH_TOKEN = 'ce9c5343f3d69d738da42f04949ea5ca'

        cl = Client(SID,AUTH_TOKEN)
        
        try :
            cl.messages.create(body= msg_, from_= '+18563861874' ,to='+91'+str(data.ph_num))
        except :
            cl.messages.create(body= msg_, from_= '+18563861874' ,to='+919345615762')
            
        return redirect('home')
        
    context = {
        'form' : form
    }

    return render(request,'msg.html' , context)

def error_404_view(request, exception):
    
    return render(request, '404_found.html')
