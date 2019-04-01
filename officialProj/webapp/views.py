from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        allsauces = ""
        allmeats = ""
        alltoppings = ""
        sauce = request.POST.getlist("sauce[]")
        protien = request.POST.getlist('protien[]')
        topping = request.POST.getlist('toppings[]')
        for meat in protien:
            allmeats = allmeats + meat + ", "
        for pieces in topping:
            alltoppings = alltoppings + pieces + ", "
        for sauces in sauce:
            allsauces = allsauces + sauces + ", "
        print("rice: " + request.POST["riceType"])
        print("protien: " + allmeats)
        print("toppings: " + alltoppings)
        print("sauces: " + allsauces )
    return render(request, 'index.html')
