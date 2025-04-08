number1 = float(input("Enter a number: "))
operation = input("-,+,x,/")
number2=float(input("Enter a number: "))
result = 5.5 
if operation == "-":
    result = number1 - number2
    print (result)
if operation == "+":
    result = number1 + number2
    print (result)
if operation == "x":
    result = number1 * number2
    print (result)
if operation == "/":
    result = number1 / number2
    print (result)