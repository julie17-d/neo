import requests

apiKey = 'kREfPQZmB3OzAK5Dzwz3OZaA8DWblhP0wMUYFMfZ'

# function to get data on a specific asteroid based on id
def getDataFromId(id):

    response = requests.get(
        'https://api.nasa.gov/neo/rest/v1/neo/' + str(id) + '?api_key=' + apiKey)
    neo = response.json()
    return neo

# function to get data on multiple asteroids based on a timeframe
def getDataFromDates(startDate, endDate):
    
    # automatically sets a 7-days timeframe if no endDate is given
    if endDate == "":
        response = requests.get(
            'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + str(startDate) + '&api_key=' + apiKey)
    else:
        response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=' + str(
            startDate) + '&end_date=' + str(endDate) + '&api_key=' + apiKey)

    neo = response.json()
    elements = neo["near_earth_objects"]
    return elements