# from functions import get_todos, write_todos
import functions
import time


timestring = time.strftime("%d/%m/%Y - %H:%M:%S")
print("It is: ",timestring)

while True:
    user_action = input("Type 'add','show','edit','complete' or 'exit' to quit : ")
    user_action = user_action.lower().strip()
    if user_action.startswith('add'):
         todo = user_action[4:]
         todos = functions.get_todos()
         todos.append(todo + "\n")
         functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos= functions.get_todos()
                #newtodos = [item.strip('\n') for item in todos]
        for index,item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                print(f"{index+1}: {item}")
    elif user_action.startswith('edit'):
        try:
            todos= functions.get_todos()
            edit_value = int(user_action[5:])
            todos[edit_value-1] = input(f"Enter your new value for {todos[edit_value-1]}")+ "\n"
            functions.write_todos(todos)
        except ValueError:
                print('Your command is not valid')
                continue
    elif user_action.startswith('complete'):
        try:
            try:
                todos = functions.get_todos()
                completed_item = int(user_action[9:])
                todos.pop(completed_item-1)
                functions.write_todos(todos)
            except IndexError:
                print('There is no item with that number')
        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Enter a valid option')

