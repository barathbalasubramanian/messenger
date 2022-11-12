from django import forms
from .models import Person,Msg

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            
            'name': forms.TextInput(attrs={'placeholder' : 'Name','class': 'form-control' , 'type' : 'text'}),
            'ph_num': forms.TextInput(attrs={'placeholder' : 'Contact Num','class': 'form-control' , 'type' : 'number'}),
        }
       
class MsgForm(forms.ModelForm) :
    
    class Meta:
        model = Msg
        fields = '__all__'
        widgets = {
                
            'msg' : forms.Textarea(attrs={'placeholder' : 'Type your Msg Here','class': 'form-control','name' : 'msg'})
        }

    
                