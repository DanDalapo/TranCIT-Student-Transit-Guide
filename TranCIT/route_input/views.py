from django.shortcuts import render
from django.db import DatabaseError
from .forms import RouteForm

def index(request):
    submitted_data = None
    error_message = None
    success_message = None

    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                # Save to Supabase (via Django ORM)
                route = form.save()
                submitted_data = {
                    'origin': route.origin,
                    'destination': route.destination,
                    'fare': route.fare,
                }
                success_message = "Route successfully saved!"
            except DatabaseError:
                error_message = "Unable to save route. Please try again later."
        else:
            error_message = "Form is invalid. Please check your input."
    else:
        form = RouteForm()

    return render(
        request,
        'route_input/index.html',
        {
            'form': form,
            'submitted_data': submitted_data,
            'success_message': success_message,
            'error_message': error_message,
        }
    )
