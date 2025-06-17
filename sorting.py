import os
import shutil
path1="D:\\organizer"#put the location of the folder which u want to sort files from
path2="D:\\organizer"#put the location of the folder which u want to sort files to (can be same as source)

#dont change anything in the below section unless you know what you are doing
files_list=os.listdir(path1)
extension_set = set()
for file in files_list:
    extension = file.split(".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue
for i in extension_set:
    print(i)
    full_path=os.path.join(path2,i)
    try:
        os.mkdir(full_path)
        print(f"Directory '{full_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{full_path}' already exists.")
        continue
    except FileNotFoundError:
        print(f"Parent directory does not exist")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
for file in files_list:
    extension = file.split(".")
    try:
        source_path = path1+"\\"+file
        destination_path=path2+"\\"+ extension[1]+"\\"+file
        shutil.move(source_path,destination_path)
    except:
        continue