from . import utils 
from json import *

tasks_dict = {}
id = 0

def help():
    print("There will be help")

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = "In progress"
        
    def __repr__(self):
        return f'Task(name="{self.name}", description="{self.description}", status="{self.status}")'

    
def add():
    global id
    
    while True:
        task_name = input(utils.Colors.yellow("Task name: "))
        if utils.ErrorChecks.empty_folder(task_name):
            break
    
    while True:
        task_description = input(utils.Colors.yellow("Task description: "))
        if utils.ErrorChecks.empty_folder(task_description):
            break
        
    new_task = Task(task_name, task_description)
    
    id += 1
    tasks_dict[id] = new_task
    
    print(utils.Colors.green(f"{task_name} task successfully created."))
    