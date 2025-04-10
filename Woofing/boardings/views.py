from django.shortcuts import render, get_object_or_404, redirect
from .models import DogBoarding
from .forms import BoardingForm

# Create your views here.


def boarding_list(request):  # Represents the HTTP request (sent by the user’s browser when they visit the page)

    # boardings = DogBoarding.objects.all()
    # boardings = DogBoarding.objects.filter(approved=True)  # Only show approved boardings

    # sort_option = request.GET.get('sort', 'price')  # Default sort by price
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    country = request.GET.get('country')
    city = request.GET.get('city')
    capacity = request.GET.get('capacity')
    sort_option = request.GET.get('sort')  # Get sorting option (if any)

    # Start with an empty queryset
    boardings = DogBoarding.objects.filter(approved=True)

    # Check if any filter is applied
    filters_applied = any([price_min, price_max, country, city, capacity])

    # Apply filters
    if price_min:
        boardings = boardings.filter(price_per_night__gte=price_min)
    if price_max:
        boardings = boardings.filter(price_per_night__lte=price_max)
    if country:
        boardings = boardings.filter(country__icontains=country)
    if city:
        boardings = boardings.filter(city__icontains=city)
    if capacity:
        boardings = boardings.filter(capacity__gte=capacity)

    # If filters were applied but no boardings match, return an empty list
    if filters_applied and not boardings.exists():
        boardings = DogBoarding.objects.none()

    # Apply sorting - Sort only if sort_option exists in request
    if sort_option:
        if sort_option == "location":
            boardings = DogBoarding.objects.filter(approved=True).order_by('location')
        elif sort_option == "capacity":
            boardings = DogBoarding.objects.filter(approved=True).order_by('capacity')  # Sorting by highest capacity first
        else:
            boardings = DogBoarding.objects.filter(approved=True).order_by("price_per_night")

    # return render(request, 'boardings/boarding_list.html', {'boardings': boardings, "sort_option": sort_option})
    return render(request, "boardings/boarding_list.html", {
        "boardings": boardings,
        "sort_option": sort_option or '',
        "price_min": price_min or '',
        "price_max": price_max or '',
        "country": country or '',
        "city": city or '',
        "capacity": capacity or ''
    })


def boarding_detail(request, boarding_id):
    boarding = get_object_or_404(DogBoarding, id=boarding_id)
    return render(request, 'boardings/boarding_detail.html', {'boarding': boarding})


def add_boarding(request):
    if request.method == 'POST':  # Check if the form was submitted (POST request)
        form = BoardingForm(request.POST, request.FILES)
        if form.is_valid():
            boarding = form.save(commit=False)
            # pension.is_approved = False  # Pension must be approved by admin

            # If no image was uploaded, make sure the image field is None
            if not boarding.image:
                boarding.image = None

            boarding.save()
            return redirect('boarding-list')

    else:  # If it's a GET request (not a form submission)
        form = BoardingForm()  # Create an empty form for the user to fill out

    return render(request, 'boardings/add_boarding.html', {'form': form})
