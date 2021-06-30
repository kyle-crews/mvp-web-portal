from django.shortcuts import render

def index(request):
    # define the variable
    number = 6
    thing = "Thing name"
    
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })