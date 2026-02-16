

try:
    total_value = float(input('Enter total value: '))
    value = float(input('Enter value: '))
    percentage = value/total_value *100
    print(f'The percentage is {percentage}')
except ValueError:
    print('You need to enter a number. Run the program again.')

waiting_list = ["john", "marry"]
try:
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except IndexError:
    print(f"{name} is not in the list")