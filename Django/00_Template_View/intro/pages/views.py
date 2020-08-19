from django.shortcuts import render

# Create your views here.
def dinner(request, menu, population):
    
    context = {
        'menu': menu,
        'population': population,
    }
    
    return render(request, 'pages/dinner.html', context)