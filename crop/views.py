from django.shortcuts import render, redirect
from django.http import HttpResponse
import joblib
import numpy as np

# Load the model once when the server starts
model_path = 'model/test.pkl'  
model = joblib.load(model_path)

def index(request):
    return render(request, 'index.html')

def refresh(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def auth(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check credentials manually (replace with your logic)
        if user_name == "Admin" and password == "admin":
            return render(request, 'after_login.html')  
        else:
            return HttpResponse("Invalid Username and password, try again.")
    else:
        return HttpResponse("Invalid request method.")


def main(request):
    return render(request, 'main.html')

def predict(request):
    if request.method == 'GET':
        # Extract form data from the GET request
        try:
            nitrogen = float(request.GET.get('nitrogen'))
            phosphorus = float(request.GET.get('phosphorus'))
            potassium = float(request.GET.get('potassium'))
            temperature = float(request.GET.get('temperature'))
            humidity = float(request.GET.get('humidity'))
            phvalue = float(request.GET.get('phvalue'))
            rainfall = float(request.GET.get('rainfall'))
            
            # Prepare input data for the model
            user_input = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, phvalue, rainfall]])
            
            # Make prediction
            predicted_crop = model.predict(user_input)[0]
            
            # Redirect to result page with input data and prediction
            return render(request, 'result.html', {
                'username': request.GET.get('username', 'User'),
                'nitrogen': nitrogen,
                'phosphorus': phosphorus,
                'potassium': potassium,
                'temperature': temperature,
                'humidity': humidity,
                'phvalue': phvalue,
                'rainfall': rainfall,
                'predicted_crop': predicted_crop
            })
        except (ValueError, TypeError):
            return HttpResponse("Invalid input. Please ensure all fields are filled correctly.")
    else:
        return HttpResponse("Invalid request method.")