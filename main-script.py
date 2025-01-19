print('Would you like to enter the calculator? Yes or No.')
isActive = input()
if isActive == 'yes':
    isActive = True
elif isActive == 'Yes':
    isActive = True
elif isActive == 'YES':
    isActive = True 
elif isActive == 'y':
    isActive = True 
elif isActive == 'Y':
    isActive = True
else:
    isActive = False

# while loop that runs the calculator
while isActive == True:
    # asks the user for operation type and defines variables
    print('would you like to add, subtract, multiply, or divide?')
    input3 = input()
    add = subtract = multiply = divide = False
    if input3 == 'add':
        add = True
        invalid = False
    elif input3 == 'subtract':
        subtract = True
        invalid = False
    elif input3 == 'multiply':
        multiply = True
        invalid = False
    elif input3 == 'divide':
        divide = True
        invalid = False
    elif input3 != 'add' or input3 != 'subtract' or input3 != 'multiply' or input3 != 'divide':
        print('Invalid operation')
        invalid = True

        while invalid == True:
            print('would you like to add, subtract, multiply, or divide?')
            input3 = input()
            if input3 == 'add':
                add = True
                invalid = False
            elif input3 == 'subtract':
                subtract = True
                invalid = False
            elif input3 == 'multiply':
                multiply = True
                invalid = False
            elif input3 == 'divide':
                divide = True
                invalid = False
            elif input3 != 'add' or input3 != 'subtract' or input3 != 'multiply' or input3 != 'divide':
                print('Invalid operation')
                invalid = True

    # gets input from user
    def getNumber():
        print('Enter a number')
        input1 = float(input())
        print('Enter another number')
        input2 = float(input())
        return input1, input2

    # calculates the result of the operation
    input1, input2 = getNumber()
    if add == True:
        print(input1 + input2)
    elif subtract == True:
        print(input1 - input2)
    elif multiply == True:
        print(input1 * input2)
    elif divide == True:
        if input1 == 0 or input2 == 0:
            print('Cannot divide by zero')
        else:
            print(input1 / input2)

    # asks the user if they would like to continue

    print('Would you like to continue? Yes or No.')
    isActive = input()
    if isActive == 'yes':
        isActive = True
    elif isActive == 'Yes':
        isActive = True
    elif isActive == 'YES':
        isActive = True
    elif isActive == 'y':
        isActive = True
    elif isActive == 'Y':
        isActive = True
    else:
        isActive = False
        print('program ended')


# Written 100% in python, just learning for now.



