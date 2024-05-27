# from functions import get_todos,write_todos
import functions
import time

now = time.strftime("%b %d, %Y %I:%M:%S %p")
print("Currently, ")
print("It is", now)
while True:
    user_action = input("Type add, view, edit, complete or exit: ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]
    
        todos = functions.get_todos()

        todos.append(todo.title()+'\n')

        functions.write_todos(todos)

        print(f"Todo: '{todo.title()}' is added to Todos")
            
    elif user_action.startswith("view"):
        todos = functions.get_todos()

        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            print(f"{index}- {item}")

    elif user_action.startswith("edit"):
        todos = functions.get_todos()

        if not todos:
            print("There are no Todos")
        else:
            try:
                number = int(user_action[5:])
                if number > len(todos):
                    print(f"There are only {len(todos)} Todos. Enter existing number.")
                else:
                    new_todo = input("Enter New Todo: ").strip() + "\n"
                    todos[number-1] = new_todo.title()
                    functions.write_todos(todos)

            except ValueError:
                print("Please Enter command in Format - Edit followed by todo number")
                continue

    elif user_action.startswith("complete"):
        todos = functions.get_todos()

        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo - '{todo_to_remove}' was removed from Todos.")
        except IndexError:
            print(f"There is not todo that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Enter a meaningful prompt")

print("Bye")