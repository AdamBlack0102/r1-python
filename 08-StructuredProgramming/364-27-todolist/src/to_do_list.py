import sys
import re

# 文件路径
file = "tasks.txt"


def add_todo_items(items):
    with open(file, 'a') as f:
        for item in items:
            f.write(f"todo:{item}\n")


def delete_todo_items(items):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            if not any(item in line for item in items):
                f.write(line)


def complete_todo_items(items):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            for item in items:
                if f"todo:{item}" in line:
                    f.write(f"completed:{item}\n")
                    break
            else:
                f.write(line)


def find_todo_items(status):
    with open(file, 'r') as f:
        for line in f:
            if line.startswith(status):
                print(line.strip())


def find_all_todo_items():
    with open(file, 'r') as f:
        for line in f:
            print(line.strip())


def to_do():
    while True:
        command = input()
        matches = re.findall(r'"([^"]*)"', command)
        if matches:
            command = re.sub(r'"([^"]*)"', '', command)
            command = command.split()
            command.extend(matches)
        else:
            command = command.split()

        if command[0] == 'todo':
            if command[1] == '-a':
                add_todo_items(command[2:])
            elif command[1] == '-d':
                delete_todo_items(command[2:])
            elif command[1] == '-c':
                complete_todo_items(command[2:])
            elif command[1] == '-f':
                find_todo_items(command[2])
            elif command[1] == '-all':
                find_all_todo_items()
            elif command[1] == '-quit':
                break
            else:
                print("fault")
        else:
            print("fault")

