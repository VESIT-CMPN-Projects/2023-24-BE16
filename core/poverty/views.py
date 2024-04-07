from django.shortcuts import render
# from poverty.model import X_encoded, X_train
import pandas as pd

from django.http import JsonResponse
from django.shortcuts import render
from .model import predict_poverty_status  


def home(request):
    return render(request, 'poverty/index.html')
# Import the function to predict poverty status

# Define the view to handle the form submission
def predict_poverty_status_view(request):
    if request.method == 'POST':
        try:
        # Retrieve input features from the form
            income = float(request.POST['income'])
            education_level = request.POST['education_level']
            family_size = float(request.POST['family_size'])
            access_healthcare = request.POST['access_healthcare']
            access_to_employment = request.POST['access_to_employment']
            access_to_education = request.POST['access_to_education']
            access_to_sanitation = request.POST['access_to_sanitation']
            access_to_water = request.POST['access_to_water']
            distance_to_market = float(request.POST['distance_to_market'])
            household_ownership = request.POST['household_ownership']
            employment_type = request.POST['employment_type']
            access_to_internet = request.POST['access_to_internet']

            # Pass input features to the predict_poverty_status function
            input_features = {
                'Income': income,
                'Education_Level': education_level,
                'Family_Size': family_size,
                'Access_to_Healthcare': access_healthcare,
                'Access_to_Employment': access_to_employment,
                'Access_to_Education': access_to_education,
                'Access_to_Sanitation': access_to_sanitation,
                'Access_to_Water': access_to_water,
                'Distance_to_Market': distance_to_market,
                'Household_Ownership': household_ownership,
                'Employment_Type': employment_type,
                'Access_to_Internet': access_to_internet
            }
            print(input_features)

            # Call the function to predict poverty status
            prediction = predict_poverty_status(input_features)
            print(prediction)

            return render(request, 'poverty/index.html', {'prediction_result': prediction})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'poverty/index.html')
# Create your views here.

