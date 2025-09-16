from modules import crud
from modules import utils


print(utils.Colors.blue("WELCOME TO TASK MANAGER CLI!"))

while True:
    action = input().strip().lower()
    
    match action:
        case "add":
            crud.add_task()
        case "test":
            crud.test()
        case "view":
            crud.view_tasks()
        case "exit":
            break
        case _:
            crud.help()