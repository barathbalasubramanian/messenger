from django_unicorn.components import UnicornView
from ..models import Person
from django.shortcuts import redirect


class EventsView(UnicornView):
    
    name = ''
    ph_num = ''
    
    def delete(self,*args) :
        
        data = Person.objects.get(id=args[0])
        data.delete()
        return redirect('home')
        
        
        
        