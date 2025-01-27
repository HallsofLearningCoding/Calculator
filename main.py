#today we'll start by learning some commonly used python operations

#Arithmetic operators: Addition +, Subtraction -, Multiplication *, Division /, Floor Division //, Exponentiation **, Modulus %

#Boolean Operators: Greater than >, Less than <, Greater than or equal to >=, Less than or equal to <=, Equal to ==, Not equal to !=

#Logical Operators: and, or, not

#Below is a program that operates similarly to a calculator. We encourage you to try it out, and complete the code/make improvements!


def main():
  print("Welcome to my calculator! Let's get started")
  a = int(input("\nEnter your first number:"))
  b = int(input("Enter your second number:"))
  choice = int(
      input(
          "\nAwesome! Let's get started. Please choose your operation.\n\n1: Addition \n2: Subtraction \n3: Multiplication \n4: Division"
      ))

  if choice == 1:
    addition(a, b)
  elif choice == 2:
    subtraction(a, b)

  elif choice == 3:
    multiplication(a, b)

  elif choice == 4:
    division(a, b)

  else:
    print("I don't understand")

  print("\nThank you for using my calculator!")
  print(
      "\nWe could make this better in many ways, for example: \n\n-Add the option to do other arithmetic operations, or even boolean operations \n-Add the option to do more than two numbers \n-Add the option to do more than one operation at a time \n\nWhat else could you do to make the calculator special?"
  )


def addition(a, b):
  print(a + b)


def subtraction(a, b):
  print(a - b)


def multiplication(a, b):
  print(a * b)


def division(a, b):
  print(a / b)


def floor_division(a, b):
  print(a // b)


def exponentiation(a, b):
  print(a**b)


def modulus(a, b):
  print(a % b)


main()
