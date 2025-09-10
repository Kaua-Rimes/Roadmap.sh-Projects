from modules import crud
from modules import utils


print(utils.Colors.blue("WELCOME TO TASK MANAGER CLI!"))

while True:
    action = input()
    
    match action:
        case "add":
            crud.Task.add()
        case _:
            crud.help()