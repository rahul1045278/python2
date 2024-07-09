def calculate(num1, num2, operator):
  """
  Performs the chosen arithmetic operation on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The chosen arithmetic operation (+, -, *, or /).

  Returns:
      The result of the calculation, or an error message for division by zero.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Cannot divide by zero."
    else:
      return num1 / num2
  else:
    return "Invalid operator. Please use +, -, *, or /."

while True:
  # Get user input
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operation (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue

  # Perform calculation and display result
  result = calculate(num1, num2, operator)
  print(f"{num1} {operator} {num2} = {result}")

  # Ask if user wants to continue
  choice = input("Do you want to perform another calculation (y/n)? ").lower()
  if choice != 'y':
    break

print("Thank you for using the calculator!")
