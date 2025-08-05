#simple python can to take user input and 2 values and compute the result

first_value = int(input('enter first value: '))
second_value = int(input('enter second value: '))
some_operand = input('enter operand: ')

match some_operand:
    case '+':
        print(first_value + second_value)
    case '-':
        print(first_value - second_value)
    case '*':
        print(first_value * second_value)
    case '/':
        print(first_value / second_value)
    case _:
        print('invalid operand')