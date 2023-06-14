from django.shortcuts import render
from django.http import HttpResponse

from math import isclose

def home(request):
    result = None
    expression = None

    if request.method == 'POST':
        first_number = float(request.POST['first_number'])
        second_number = float(request.POST['second_number'])
        operation = request.POST['operation']

        if operation == 'add':
            result = first_number + second_number
            expression = f"{first_number} + {second_number}"
        elif operation == 'subtract':
            result = first_number - second_number
            expression = f"{first_number} - {second_number}"
        elif operation == 'multiply':
            result = first_number * second_number
            expression = f"{first_number} * {second_number}"
        elif operation == 'divide':
            if second_number != 0:
                result = first_number / second_number
                expression = f"{first_number} / {second_number}"
            else:
                result = "Division by zero is not allowed!"
                expression = ""

    if result is not None and isclose(result, int(result)):
        result = int(result)

    return render(request, 'calculations/home.html', {'result': result, 'expression': expression})
