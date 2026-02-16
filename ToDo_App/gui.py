import functions
import FreeSimpleGUI as Sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

Sg.theme('DarkRed1')

label =Sg.Text("Type in a To-Do")
input_box = Sg.InputText(tooltip = "Enter todo",key="todo")
add_button =  Sg.Button("Add")
list_box = Sg.Listbox(functions.get_todos(),key="todos",
                      enable_events=True,
                      size=(45,10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit",key="Exit")
clock = Sg.Text("",key="clock")


window = Sg.Window("My To-Do App",
                   layout= [[clock],[label],[input_box,add_button],[list_box,edit_button,complete_button],
                            [exit_button]],
                   font=("Helvetica",10))

while True:
    event,values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=[todo.strip() for todo in todos])
        case "Edit":
            try:
                todo_to_edit = values['todos'][0] + "\n"
                new_todo = values['todo'].strip() + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=[todo.strip() for todo in todos])
            except IndexError:
                Sg.popup("Please select an item first")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:

                todo_complete = values['todos'][0] + "\n"
                print(todo_complete)
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window["todos"].update(values=[todo.strip() for todo in todos])
                window["todo"].update(value="")
            except IndexError:
                Sg.popup("Please select an item first")
        case "Exit":
            break
        case Sg.WIN_CLOSED:
            break


window.close()