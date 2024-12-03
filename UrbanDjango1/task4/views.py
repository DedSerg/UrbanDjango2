from django.shortcuts import render
from django.views.generic import TemplateView

class Platform_game(TemplateView):
    template_name = 'platform.html'



class Cart_game(TemplateView):
    template_name = 'cart.html'

def menu_game(request):
    mydict = {'games': ["Скандинавский бой", "Каркассон", "Бэнг!"]}

    context={
         'mydict':mydict,
    }
    return render(request, 'games.html', context)

