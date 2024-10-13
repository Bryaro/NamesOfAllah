from django.shortcuts import render, redirect, get_object_or_404
from .models import NameOfAllah

def home(request):
    return render(request, 'names99/home.html')

def process_learning(request):
    if request.method == "POST":
        names_per_day = request.POST.get('names_per_day')

        # Check if names_per_day is not None and can be converted to an integer
        if names_per_day is None or not names_per_day.isdigit():
            return render(request, 'names99/home.html', {
                'error_message': "Please select the number of names to learn."
            })

        names_per_day = int(names_per_day)

        # Initialize learned names in session if not already set
        if 'learned_names' not in request.session:
            request.session['learned_names'] = 0

        total_learned = request.session['learned_names']
        names = NameOfAllah.objects.all()[total_learned:total_learned + names_per_day]

        # Update learned names in the session
        request.session['learned_names'] += len(names)
        if request.session['learned_names'] > 99:
            request.session['learned_names'] = 99
        request.session.modified = True

        learned_names = request.session['learned_names']
        progress_percentage = (learned_names / 99) * 100

        # Ensure the names are passed to the template for display
        return render(request, 'names99/learning_page.html', {
            'names': names,
            'learned_names': learned_names,
            'progress_percentage': progress_percentage,
            'read_names': NameOfAllah.objects.filter(read=True).values_list('id', flat=True)  # Get IDs of read names
        })
    else:
        return render(request, 'names99/home.html')


def reset_learning(request):
    if request.method == "POST":
        if 'learned_names' in request.session:
            del request.session['learned_names']
    return render(request, 'names99/home.html')

def name_detail(request, name_id):
    name = get_object_or_404(NameOfAllah, id=name_id)
    return render(request, 'name_detail.html', {'name': name})

def mark_as_read(request):
    if request.method == "POST":
        read_names = request.POST.getlist('read_names')
        
        # Update the read status of selected names
        if read_names:
            NameOfAllah.objects.filter(id__in=read_names).update(read=True)

    return redirect('learning_page')  # Redirect back to the learning page


def learning_page(request):
    learned_names = request.session.get('learned_names', 0)
    names_per_day = 4  # Default value or retrieve from session if needed

    names = NameOfAllah.objects.all()[learned_names:learned_names + names_per_day]

    return render(request, 'names99/learning_page.html', {
        'names': names,
        'learned_names': learned_names,
    })
