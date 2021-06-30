from django.shortcuts import render

def index(request):
    # define the variable
    number = 6
    # pass the variable to the view
    return render(request, 'index.html', {
        'number': number,
    })