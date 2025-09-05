from modules import crud


print("WELCOME TO TASK MANAGER CLI")

while True:
    action = input()
    
    match action:
        case "add":
            crud.Task.add()
        case _:
            crud.help()