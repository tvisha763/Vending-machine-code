from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.contrib import messages
from django.contrib import messages
import random
import ast
import read


# Create your views here.

def setSnack(s):
    with open("snack.txt", "w") as file:
        file.write(s)
        file.flush()


def getSnack():
    with open("snack.txt", "r") as file:
        return file.read()
    
    
def setPrice(s):
    with open("price.txt", "w") as file:
        file.write(s)
        file.flush()

def getPrice():
    with open("price.txt", "r") as file:
        return int(file.read())

def setCorrect(s):
    with open("correct_answer.txt", "w") as file:
        file.write(s)
        file.flush()

def getCorrect():
    with open("correct_answer.txt", "r") as file:
        return file.read()

def setPaid():
    with open("paid.txt", "w") as file:
        file.write("True")
        file.flush()

def setNotPaid():
    with open("paid.txt", "w") as file:
        file.write("False")
        file.flush()

def getPaid():
    with open("paid.txt", "r") as file:
        return ast.literal_eval(file.read())
    





def pick_snack(request):
    return render(request, 'pick_snack.html')


def buy(request):
    if request.method == "POST":
        snack = request.POST.get('snack')
        price = request.POST.get('price')

    print(snack)
    with open("snack.txt", "w") as file:
        file.write(snack)
    print(getSnack())

    setSnack(snack)
    setPrice(price)
    setNotPaid()
    return redirect('pay')

def pay(request):
    return render(request, 'pay.html')

def paid(request):
    read.pay()
    if getPaid():
        return redirect('ask_math')
    else:
        messages.error(request, "Please pay before pressing the 'paid' button.")
        return redirect('pay')

def ask_math(request):
    with open("math_questions.txt", "r") as file:
        content = file.read()


    questions = ast.literal_eval(content)



    question = ast.literal_eval(random.choice(questions))

    setCorrect(question["correct_choice"])

    context = {
        "question" : question["question"],
        "a" : question["choices"][0],
        "b" : question["choices"][1],
        "c" : question["choices"][2],
        "d" : question["choices"][3],
    }

    return render(request, 'ask_math.html', context)




# print("correct answer: " + correct_answer)

def response(request):
    if request.method == "POST":
        response = request.POST.get('response')
        if response == getCorrect():
            return redirect('correct')
        else:
            return redirect('wrong')
        

def dispose():
    snack = getSnack()
    read.rotate(snack, 512, direction=1)


def correct(request):
    dispose()
    return render(request, 'correct.html')

def wrong(request):
    return render(request, 'wrong.html')

