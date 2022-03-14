from typing import overload
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')


# def dinner(request, menu, numberofpeople):
#     context = {
#         'menu': menu,
#         'numberofpeople': numberofpeople,
#     }
#     return render(request, 'dinner.html', context)

# def dinner(request):
#     menu = request.GET.get('menu')
#     numberofpeople = request.GET.get('numberofpeople')
#     context = {
#         'menu': menu,
#         'numberofpeople': numberofpeople,
#     }
#     return render(request, 'dinner.html', context)

def dinner(request, menu=None, numberofpeople=None):
    if menu == None and numberofpeople == None:
        menu = request.GET.get('menu')
        numberofpeople = request.GET.get('numberofpeople')

    context = {
        'menu': menu,
        'numberofpeople':numberofpeople,
    }
    return render(request, 'dinner.html', context)
    
    
       