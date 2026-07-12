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
              "delete task\n"
              "3:mark task as done\n"
              "4:exit")
        try:
            command = int(input("command: "))
        except :
            print("!!!!!invalid command!!!!!!")
            continue
        if command == 4:
            kill_main()
        if command == 1:
            pass
            add_task()
        if command == 2:
            show_task()

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







