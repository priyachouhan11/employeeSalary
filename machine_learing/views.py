import numpy as np
from django.shortcuts import render
from .utils import loaded_model

def home(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        try:
            features = []
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken':  
                    print(f"Processing input value: {value[0]}")  
                    try:
                        features.append(float(value[0])) 
                    except ValueError:
                        print("Invalid input detected.") 
                        return render(request, 'index.html', {'error': 'Please enter numeric values only.'})

            
            final_feature = [np.array(features)]
            #print(f"Final feature array: {final_feature}") 
            prediction = loaded_model.predict(final_feature)  
            output = round(prediction[0])
            #print(f"Prediction output: {output}") 
            return render(request, 'index.html', {'output': f'Employee Salary should be ₹ {output}'})
        
        except Exception as e:
            print(f"Error occurred: {e}")
            return render(request, 'index.html', {'error': 'An error occurred. Please try again.'})
    
    else:
        print("GET request received, rendering home.") 
        return render(request, 'index.html')
