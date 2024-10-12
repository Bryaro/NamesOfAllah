# names99/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'names99/home.html')

def process_learning(request):
    if request.method == "POST":
        names_per_day = request.POST.get('names_per_day')
        return render(request, 'names99/learning_page.html', {'names_per_day': names_per_day})
