def calculate(a,b,operation):
  if operation not in "+-*/":
    return "Please select an operation(+,-,*,/)"
  if operation == "+":
    return (str(a) + " + " + str(b) + " = " + str(a+b))
  elif operation == "-":
    return (str(a) + " - " + str(b) + " = " + str(a-b))
  elif operation == "*":
    return (str(a) + " * " + str(b) + " = " + str(a*b))
  else:
    return (str(a) + " / " + str(b) + " = " + str(a/b))

while True:
  try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    operation = input("Selecet your operation(+,-,*,/): ")
    print(calculate(a,b,operation))
  except:
    print("Please enter the number!")
