from .forms import dateForm

def getDates(request):
    
    # get data from form if there is a post request
    if request.method == 'POST':
        form = dateForm(request.POST)
        if form.is_valid():
            startDate = form['startDate'].value()
            endDate = form["endDate"].value()

            # checks that the startDate isn't set after the endDate
            if startDate <= endDate:
                validDate = True

                return [startDate, endDate, validDate] 
    
    form = dateForm()
    validDate = False

    return [form["startDate"].value(), form["endDate"].value(), validDate]