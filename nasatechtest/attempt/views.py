from django.shortcuts import render

from .sortData import createAsteroidObjects, getLastPassages
from .forms import dateForm

def index(request):

    data = createAsteroidObjects(request)

    asteroids = data[0]

    validDate = data[1]

    # adds a message to main page if no valid date is given
    if validDate == False:
        message = "Here are asteroids that passed Earth today. Enter valid dates to see another timeframe."
    else:
        message = False

    if request.method == 'POST':
        form = dateForm(request.POST)
    else:
        form = dateForm()


    return render(request, 'index.html', {'form': form, 'asteroids': asteroids, 'message': message})


def asteroid(request, id):

    asteroid = getLastPassages(id)

    lastPassages = asteroid[0]
    name = asteroid[1]

    return render(request, 'asteroid.html', {'id': id, 'passages': lastPassages, 'name': name})