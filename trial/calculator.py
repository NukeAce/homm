import re

print("Calculator")
print ("type quit to exit\n")
previous = 0
run = True

def perform_math():
    global run
    global previous
    if previous ==0:
        equation = input ("Enter equation: ")
    else:
        equation= input(str(previous))
    if equation == "quit":
        print("goodbye human")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)

while run:
    perform_math()