from . import utils 
import json


def help():
    print("There will be help")

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = "In progress"
        
    def __repr__(self):
        return f'Task(name="{self.name}", description="{self.description}", status="{self.status}")'


def add_task():
    while True:
        task_name = input(utils.Colors.yellow("Task name: "))
        if utils.ErrorChecks.empty_folder(task_name):
            break
    
    while True:
        task_description = input(utils.Colors.yellow("Task description: "))
        if utils.ErrorChecks.empty_folder(task_description):
            break
        
    tasks_data = []
    
    try:
        with open("database.json", mode="r", encoding="utf-8") as read_file:
            tasks_data = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    
    next_id = 1
    if tasks_data:
        next_id = tasks_data[-1]["id"] + 1
        
    new_task_dict = {
        "id": next_id,
        "name": task_name,
        "description": task_description,
        "status": "In progress"
    }

    tasks_data.append(new_task_dict)
    
    with open("database.json", mode="w", encoding="utf-8") as write_file:
        json.dump(tasks_data, write_file, indent=4)
    
    try:
        with open("database.json", mode="w", encoding="utf-8") as write_file:
            json.dump(tasks_data, write_file, indent=4)
    except IOError as e:
        print(utils.Colors.red(f"ERROR!{e} Task coud not be created."))
        
    print(utils.Colors.green(f"{task_name} task successfully created."))

def view_tasks():
    try:
        with open("database.json", mode="r", encoding="utf-8") as read_file:
            tasks_data = json.load(read_file)
    except(FileNotFoundError, json.JSONDecodeError):
        print(utils.Colors.red("No task found."))
        return
    
    if not tasks_data:
        print(utils.Colors.red("No task found."))
        return
    
    print(json.dumps(tasks_data, indent=4))
    
def update_task():
    try:
        with open("database.json", mode="r", encoding="utf-8") as read_file:
            tasks_data = json.load(read_file)
    except(FileNotFoundError, json.JSONDecodeError):
        print(utils.Colors.red("No task found."))
        return
    
    view_tasks()
    
    if not tasks_data:
        print(utils.Colors.red("No task found."))
        return
    
    while True:
        try:
            option = int(input("Chose the ID of the task you would like to update. "))
            if 1 <= option <= len(tasks_data):
                break 
            else:
                print(utils.Colors.red("ERROR! Please, insert a valid ID number."))
        except ValueError:
            print(utils.Colors.red("ERROR! Please, insert a valid ID number."))
            
    while True:
        task_name = input(utils.Colors.yellow("Task name: "))
        if utils.ErrorChecks.empty_folder(task_name):
            break

    while True:
        task_description = input(utils.Colors.yellow("Task description: "))
        if utils.ErrorChecks.empty_folder(task_description):
            break
                
    tasks_data[option -1] = {
    "id": option,
    "name": task_name,
    "description": task_description,
    "status": "In progress"
    }

    try:
        with open("database.json", mode="w", encoding="utf-8") as write_file:
            json.dump(tasks_data, write_file, indent=4)
            print(utils.Colors.green(f"'{task_name}' task successfully updated."))
    except IOError as e:
        print(utils.Colors.red(f"ERROR!'{e}'Task coud not be updated."))    
