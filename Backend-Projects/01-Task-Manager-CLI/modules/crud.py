from . import utils 

def help():
    print("There will be help")

class Task:
    def __init__(self):
        pass
    
    def add():
        while True:
            task_name = input(utils.Colors.yellow("Task name: "))
            if utils.ErrorChecks.empty_folder(task_name):
                break
        
        while True:
            task_description = input(utils.Colors.yellow("Task description: "))
            if utils.ErrorChecks.empty_folder(task_description):
                break
        