#simple python can to take user input and 2 values and compute the result

try:
    first_value = int(input('enter first value: '))
    second_value = int(input('enter second value: '))
except ValueError:
    print("Error: Please enter valid integers for both values.")
    exit()

some_operand = input('enter operand: ')

match some_operand:
    case '+':
        print(first_value + second_value)
    case '-':
        print(first_value - second_value)
    case '*':
        print(first_value * second_value)
    case '/':
        if second_value == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(first_value / second_value)
    case _:
        print('invalid operand')