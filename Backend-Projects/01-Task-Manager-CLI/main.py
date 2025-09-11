from modules import crud
from modules import utils


print(utils.Colors.blue("WELCOME TO TASK MANAGER CLI!"))

while True:
    action = input()
    
    match action:
        case "add":
            crud.add()
        case _:
            crud.help()