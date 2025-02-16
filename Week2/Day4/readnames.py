import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir,"names.txt")


with open (file_path,encoding = "utf-8") as f :
    file = f.readlines()
    # for name in names:
    #     print(name.strip())
    list_of_lists = []