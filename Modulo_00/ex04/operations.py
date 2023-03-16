import sys

def operate(num1, num2):
    Sum: num1+num2 
    Difference: num1-num2
    Product: num1*num2
    Quotient: num1/num2
    Remainder: num1%num2
    print("Sum:\t\t" + str(num1+num2))
    print("Difference:\t" + str(num1-num2))
    print("Product:\t" + str(num1*num2))
    print("Quotient:\tERROR (division by zero)") if num2 == 0 else print("Quotient:\t" + str(num1/num2))
    print("Remainder:\tERROR (modulo by zero)") if num2 == 0 else print("Remainder:\t" + str(num1%num2))


if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    exit(0)
elif len(sys.argv) < 3:
      print("Usage: python operations.py <number1> <number2>\nExample: \n\tpython operations.py 10 3")
else:
    try:
        operate(int(sys.argv[1]), int(sys.argv[2]))
    except:
        print("Both arguments must be numbers")

