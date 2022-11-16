from datetime import datetime

from .asteroidClass import Asteroid
from .getDates import getDates
from .getData import getDataFromDates, getDataFromId


def getNextPassage(id):

    asteroid = getDataFromId(id)

    for info in asteroid["close_approach_data"]:

        # returns the next passage of the asteroid
        if datetime.strptime(info["close_approach_date"], "%Y-%m-%d") > datetime.today():
            return info["close_approach_date"]


def getLastPassages(id):

    fivePassages = []
    asteroid = getDataFromId(id)

    for info in asteroid["close_approach_data"]:

        # gets all passages of an asteroid before today's date...
        if datetime.strptime(info["close_approach_date"], "%Y-%m-%d") < datetime.today():
            fivePassages.append(info["close_approach_date"])

    # ... and sort them to only keep the five most recent
    fivePassages.sort()
    fiveLast = fivePassages[-5:]

    name = asteroid["name"]
    return [fiveLast, name]


def getElements(request):

    dates = getDates(request)
    validDate = dates[2]

    # uses today's date if no date or an invalid date is provided
    if validDate == False or dates[0] == None or dates[1] == None:
        startDate = datetime.today()
        endDate = datetime.today()
    else:
        startDate = dates[0]
        endDate = dates[1]
    
    elements = getDataFromDates(startDate, endDate)
    
    return [elements, validDate]


def createAsteroidObjects(request):

    asteroids = []

    data = getElements(request)
    validDate = data[1]
    elements = data[0]

    for date in elements.values():
        for object in date:
            id = object["id"]
            nextPassage = getNextPassage(id)

            # creates list of Asteroid objects with all the info needed on the main page
            asteroid = Asteroid(object["name"], object["estimated_diameter"]["meters"]["estimated_diameter_min"], object["estimated_diameter"]["meters"]["estimated_diameter_max"], object["close_approach_data"][0]["miss_distance"]["kilometers"], id, nextPassage)
            asteroids.append(asteroid)

    return [asteroids, validDate]