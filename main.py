import json
import os
from datetime import datetime
import re
current_path = os.getcwd()
if not os.path.exists(f"{current_path}/to_do"):
    os.mkdir(f"{current_path}/to_do")











def main():
    print("to-do list: what do you want to do today?")
    while True:
        print("enter command\n"
              "1:add task\n"
              "2:show tasks\n"
              "3:mark task as done\n"
              "4:exit\n"
              "5:delete task")
        try:
            command = int(input("command: "))
        except :
            print("!!!!!invalid command!!!!!!")
            continue
        if command == 1:
            add_task()
        if command == 2:
            show_task()
        if command == 5:
            delete_task()
        if command == 4:
            kill_main()
        if command == 3:
            mark_as_done()


def mark_as_done():
    if os.path.exists(f"{current_path}/to_do"):
        files = []
        all_files = os.listdir(f"{current_path}/to_do")
        for file in all_files:
            if file.endswith(".json"):
                files.append(file)
                print(f"task_{len(files)}:{file}")
        if not files:
            print("!!!No tasks found!!!")
            return
        print(f"enter number of file you want to mark as done:")
        while True:
            try:
                command = int(input("number: "))
                if command <= 0:
                    print("!!!invalid number!!!\n"
                          "try 1-99")
                else:
                    break
            except :
                print("!!!invalid number!!!")
        try:
            file_mark_as_done = files[command-1]
            with open(f"{current_path}/to_do/{file_mark_as_done}", "r") as file:
                file_data = json.load(file)
                file_data["done"] = True
            with open(f"{current_path}/to_do/{file_mark_as_done}", "w") as file:
                json.dump(file_data, file, indent=4)
                print(f"done file: {file_mark_as_done}")

        except :
            print("!!!invalid file!!!")



def delete_task():
    if os.path.exists(f"{current_path}/to_do"):
        files = []
        all_files = os.listdir(f"{current_path}/to_do")
        for file in all_files:
            if file.endswith(".json"):
                files.append(file)
                print(f"task_{len(files)}:{file}")
        if not files:
            print("!!!No tasks found!!!")
            return
        print(f"enter number of file you want to delete:")
        while True:
            try:
                command = int(input("number: "))
                if command <= 0:
                    print("!!!invalid number!!!\n"
                          "try 1-99")
                else:
                    break
            except :
                print("!!!invalid number!!!")
        try:
            file_to_delete = files[command-1]
            path_f_t_delete = f"{current_path}/to_do/{file_to_delete}"
            os.remove(path_f_t_delete)
            print(f"deleted file: {file_to_delete}")
        except :
            print("!!!invalid file!!!")




def show_task():
    print("all your tasks:")
    if os.path.exists(f"{current_path}/to_do"):
        all_files = os.listdir(f"{current_path}/to_do")
        json_files = [file for file in all_files if file.endswith(".json")]
        if not json_files:
            print("!!!!!no any json file!!!!!")
        else:
            print(f"detected files: {len(json_files)}")
            for file in json_files:
                with open(f"{current_path}/to_do/{file}", "r") as f:
                    file_data = json.load(f)
                    print(file_data)

    else:
        print("!!!!!invalid file!!!!!!\n"
              "!!!!!no files in directory!!!!!")





def add_task():
    print("!add task name!\n"
          "!!!ONLY IN ENGLISH!!!")
    task_name = input("task name: ").strip()
    clean_name = re.sub(r'[^a-zA-Z0-9а-яА-ЯёЁ\s_-]', '', task_name)
    clean_name = clean_name.strip().replace(" ", "_")
    if not clean_name:
        clean_name = "task"
    print("!add task!")
    task_goal = input("task goal: ")
    get_date = datetime.now()
    date = get_date.strftime("%Y-%m-%d")
    task = {f"task": f"{clean_name}", f"goal": task_goal, f"done": False}
    with open(f"{current_path}/to_do/{date}_{clean_name}.json", "w") as f:
        json.dump(task, f, indent=4)



def kill_main():
    exit()


if __name__ == "__main__":
    main()







