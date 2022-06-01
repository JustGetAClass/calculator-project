#Calculator

from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2


operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide
            }


def calculator():
  print(logo)

  num1 = float(input("What is your first number? "))
    
  for symbol in operation:
    print(symbol)
  
  math_continue = True 
  while math_continue:
    operation_symbol = input("pick an operation: ")
    num2 = float(input("What is your next number? "))
    
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    proceed = input("Do you want to proceed? y or n start fresh: ")
    if proceed == "y":
      num1 = answer
    else:
      math_continue = False
      calculator()

calculator()