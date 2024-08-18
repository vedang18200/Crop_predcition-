import joblib
import numpy as np


model_path = 'model/test.pkl'
model = joblib.load(model_path)

def get_user_input():
    N = float(input("Enter Nitrogen content in the soil (N): "))
    P = float(input("Enter Phosphorus content in the soil (P): "))
    K = float(input("Enter Potassium content in the soil (K): "))
    temperature = float(input("Enter Temperature (°C): "))
    humidity = float(input("Enter Humidity (%): "))
    ph = float(input("Enter pH value of the soil: "))
    rainfall = float(input("Enter Rainfall (mm): "))
    
    
    return np.array([[N, P, K, temperature, humidity, ph, rainfall]])


user_input = get_user_input()


predicted_crop = model.predict(user_input)
print(f"The recommended crop is: {predicted_crop[0]}")
