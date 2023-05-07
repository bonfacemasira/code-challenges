def maximum_number():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    if num1 > num2:
        print(f'The first number({num1}) is the maximum number')
    elif num2 > num1:
        print(f'The second number({num2}) is the maximum number')
    else:
        print(f'The first number({num1}) is equal to the second number({num2})')

maximum_number()