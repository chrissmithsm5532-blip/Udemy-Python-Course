import function
import FreeSimpleGUI as Sg
import time

from functions import write_todos
Sg.theme('DarkRed1')

label =Sg.Text("Type in a To-Do")
input_box = Sg.InputText(tooltip = "Enter todo",key="todo")
add_button =  Sg.Button(size=2,image_source="add.png",mouseover_colors="Red1",tooltip="Add To Do",key="Add")
list_boxex = Sg.Listbox(function.get_todose(),key="todos",
                      enable_events=True,
                      size=(45,10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button(image_source="complete.png",tooltip="Complete To-Do",key="Complete")
exit_button_ex = Sg.Button("Exit..",key="Exit")
clock = Sg.Text("",key="clock")


window = Sg.Window("My To-Do App",
                   layout= [[clock],[label],[input_box,add_button],[list_boxex,edit_button,complete_button],
                            [exit_button_ex]],
                   font=("Helvetica",10))

while True:
    event,values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%H:%M:%S"))
    match event:
        case "Add":
            todos = function.get_todose()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todose(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = function.get_todose()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todose(todos)
                window["todos"].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item first")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todo_complete = values['todos'][0]
                print(todo_complete)
                todos = function.get_todose()
                todos.remove(todo_complete)
                function.write_todose(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                Sg.popup("Please select an item first")
        case "Exit":
            break
        case Sg.WIN_CLOSED:
            break


window.close()