import os
logo = r"""
 _____________________
|  _________________  |
| | Calculator   0. | |  
| |_________________| | 
|  ___ ___ ___   ___  |  
| | 7 | 8 | 9 | | + | |  
| |___|___|___| |___| |  
| | 4 | 5 | 6 | | - | |  
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| |  
| | . | 0 | = | | / | | 
| |___|___|___| |___| | 
|_____________________|
"""

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("Whats the  first number: "))
    while should_continue:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick a operation:")
        num2 = float(input("Whats the second number: "))
        first_result = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {first_result}")
        choice = input(f"Type 'y' to continue calculation with {first_result}, or Type 'n' to start a new calculation.")
        if choice == 'y':
            num1 = first_result
        else:
            should_continue = False
            os.system("cls")
            calculator()
calculator()