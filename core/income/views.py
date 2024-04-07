from django.http import JsonResponse
from django.shortcuts import render
from .models import predict_farming_income_function
from joblib import load
# import pandas as pd

# Load your trained model and preprocessor
model = None  # Initialize as None

def load_model():
    global model
    model = load('finalized_model.sav')  # Replace with the actual path to your model file

# Call the load_model function when your Django app starts
load_model()

def home(request):
    return render(request, 'income/index.html')

def predict_farming_income(request):
    print("Entered function")
    if request.method == 'POST':
        try:
            # Get input features from the form submission
            historical_income = float(request.POST.get('historical_income'))
            weather_forecasts = float(request.POST.get('weather_forecasts'))
            crop_type = request.POST.get('crop_type')
            market_conditions = float(request.POST.get('market_conditions'))
            investment_machinery = float(request.POST.get('investment_machinery'))
            expenses = float(request.POST.get('expenses'))
            profit_margin = float(request.POST.get('profit_margin'))

            # Use the input features to make predictions using your model
            input_features = {
                'Historical_Income': historical_income,
                'Weather_Forecasts': weather_forecasts,
                'Crop_Type': crop_type,
                'Market_Conditions': market_conditions,
                'Investment_Machinery': investment_machinery,
                'Expenses': expenses,
                'Profit_Margin': profit_margin,
            }

            print("Input Features:", input_features)

            # Call your prediction function or model.predict() here
            predicted_income = predict_farming_income_function(input_features)

            print("HERE")

            # Return predictions in the response
            return render(request, 'income/index.html', {'predicted_income': predicted_income})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'income/index.html')
