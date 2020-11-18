from django.shortcuts import render, redirect
from .forms import CityForm
from .models import savecities
#Create your views here

#home page
def tropical_cities_home(request):
    return render(request, 'BeachApp/BeachApp_home.html')


#popular cities page
def tropical_cities_popular(request):
    return render(request, 'BeachApp/BeachApp_pop_cities.html')


#save cities page
def save_tropical_cities(request):
    form = CityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('TropicalCitiesHome')
    else:
        print(form.errors)
        form = CityForm()

    context = {'form': form}
    return render(request, 'BeachApp/BeachApp_save_tropical_cities.html', context)


#view saved cities page
def tropical_cities_wish_list_index(request):
    mycities = savecities.objects.all()
    return render(request, 'BeachApp/BeachApp_wish_list_index.html', {"mycities": mycities})


def tropical_cities_details(request, pk):
    pk = int(pk)
    save_cities = savecities.objects.get(id=pk)
    return render(request, 'BeachApp/BeachApp_details.html', {"save_cities" : save_cities})

#hotels page
def tropical_cities_book_hotels(request):
    return render(request, 'BeachApp/BeachApp_hotels.html')