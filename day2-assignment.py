# Assignment 1 - Calculator
input1 = float(input('Input your first number: '))
input2 = input('Input your operand (+,-,*,/): ')
input3 = float(input('Input your second number: '))

if (input2 == '*'):
    print(input1 * input3)
elif (input2 == '-'):
    print(input1 - input3)
elif (input2 == '+'):
    print(input1 + input3)
elif (input2 == '/'):
    if input3 == 0:
        print('Cannot divide by zero')
    else:
        print(input1 / input3)
else:
    print('Please enter a valid operand (+,-,*,/)')

# Assignment 2 - Even Odd
numinput = int(input("Please enter in a number: "))
if (numinput % 2 == 0):
    print("even")
else:
    print('odd')

# Assignment 3 - Fizz Buzz
inputFBNumber = float(input("Please enter in a number: "))


if (inputFBNumber % 3 == 0) & (inputFBNumber % 5 == 0):
    print('Fizz Buzz')
elif (inputFBNumber % 3 == 0):
   print('Fizz')
elif (inputFBNumber % 5 == 0):
   print('Buzz')
else:
    print("")
