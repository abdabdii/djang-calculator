from django.shortcuts import render, get_object_or_404, redirect
from .models import Calculation
from .forms import CalcForm


from django.views import View

def calculate(num1,num2,operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "x":
        return num1*num2
    elif operation == "/":
        return num1/num2
    else:
        return pow(num1,num2)

class CalculatorView(View):
    def get(self, request):
        form = CalcForm()
        return render(request , 'calculator.html' , {'form':form})

    def post(self,request):
        form = CalcForm(request.POST or None)
        if form.is_valid():
            calculation = form.save(commit=False)
            calculation.result = calculate(calculation.number1,
                                          calculation.number2,
                                          calculation.operation.symbol)
            calculation.save()
            return redirect('result',pk=calculation.id)
        return render(request , 'calculator.html' , {'form':form})
        
            
        

def result_view(request,pk):
    calculation = get_object_or_404(Calculation,pk=pk)
    return render(request , 'result.html' , {'obj':calculation})


        
    