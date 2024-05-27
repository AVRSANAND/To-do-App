import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do: ")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(type(event))
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+'\n')
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break


window.close()
