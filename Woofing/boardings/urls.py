from django.urls import path, include
from . import views
from .views import boarding_list, boarding_detail, add_boarding

urlpatterns = [  # A list of all the URLs for this app
    path('', boarding_list, name='boarding-list'),

    # path('boardings/<int:boarding_id>/', boarding_detail, name='boarding_detail'),

    path('<int:boarding_id>/', boarding_detail, name='boarding_detail'),

    # path('add-boarding/', views.add_boarding, name='add_boarding'),
    # path('add-boarding/', add_boarding, name='add_boarding'),  # This line tells Django: “When someone visits the site,
                                            # pass them to the boardings app’s URL file to decide what to show.”

    path('add-boarding/', add_boarding, name='add_boarding'),
]