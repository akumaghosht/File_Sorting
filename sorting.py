import os
import shutil
import tkinter as tk
from tkinter import filedialog,ttk
def selector1():
    select_directory(1)
def selector2():
    select_directory(2)
def select_directory(x):
    # x=1
    selected_directory = filedialog.askdirectory(
        initialdir="/",
        title="Select a Directory"
    )
    if(x==1):
        if selected_directory:
            directory_path_label1.config(text=f"{selected_directory}")
            path1=selected_directory
            print(f"Directory selected: {selected_directory}")
        else:
            directory_path_label1.config(text="No Directory Selected")
            print("No directory was selected.")
    elif(x==2):
        if selected_directory:
            directory_path_label2.config(text=f"{selected_directory}")
            path2=selected_directory
            print(f"Directory selected: {selected_directory}")
        else:
            directory_path_label2.config(text="No Directory Selected")
            print("No directory was selected.")

def organize_files():
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
def organize_files2():
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
def extractor():
    print("im here to fix syntax")
def on_option_selected(event):
    """
    Callback function when an option is selected from the Combobox.
    Updates the label to show the selected option.
    """
    selected_option = option_selector.get() # Get the currently selected value from the Combobox
    if(selected_option==op1):
        func_selector=1
        executioner=ttk.Button(
            main_frame,
            text="Organize",
            command=organize_files
            )
        executioner.pack()
    elif(selected_option==op2):
        func_selector=2
        executioner=ttk.Button(
            main_frame,
            text="Organize",
            command=organize_files2
            )
        executioner.pack()
    elif(selected_option==op3):
        func_selector=3
        executioner=ttk.Button(
        main_frame,
        text="Extract",
        command=extractor
        )
        executioner.pack()
    print(f"Option selected: {func_selector}")

func_selector=0
path1="\\"#put the location of the folder which u want to sort files from
path2="\\"#put the location of the folder which u want to sort files to (can be same as source)
root=tk.Tk()
root.title("File Organizer")
root.geometry("800x400")
style=ttk.Style(root)
style.theme_use('clam')
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill="both")
source_text = ttk.Label(
    main_frame,
    text="Source: ",
    wraplength=400, # Wrap text if it's too long
    font=("Inter", 10)
)
source_text.pack()
directory_path_label1 = ttk.Label(
    main_frame,
    text="No Directory Selected",
    wraplength=400, # Wrap text if it's too long
    font=("Inter", 10)
)
directory_path_label1.pack()
select_button1 = ttk.Button(
    main_frame,
    text="Browse",
    command=selector1 # Assign the function to be called when button is clicked
)

select_button1.pack()
destination_text = ttk.Label(
    main_frame,
    text="Destination: ",
    wraplength=400, # Wrap text if it's too long
    font=("Inter", 10)
)
destination_text.pack()
directory_path_label2 = ttk.Label(
    main_frame,
    text="No Directory Selected",
    wraplength=400, # Wrap text if it's too long
    font=("Inter", 10)
)
directory_path_label2.pack()
select_button2 = ttk.Button(
    main_frame,
    text="Browse",
    command=selector2 # Assign the function to be called when button is clicked
)
select_button2.pack()
option_label = ttk.Label(
    main_frame,
    text="Choose an option:",
    font=("Inter", 10)
)
option_label.pack(pady=10)
op1="organize all individual files available by their type"
op2="organize all files available including files inside folders"
op3="extract files of a particular type"
# Define the list of options for the Combobox
options = [op1, op2, op3]

# Create the Combobox (dropdown menu)
option_selector = ttk.Combobox(
    main_frame,
    values=options, # Set the available options
    state="readonly", # Make it read-only so users can only select from the list
    font=("Inter", 10)
)
option_selector.set("Select an option") # Set a default placeholder text
option_selector.pack(pady=5)
option_selector.bind("<<ComboboxSelected>>", on_option_selected)

# Label to display the selected option from the Combobox


root.mainloop()
#dont change anything in the below section unless you know what you are doing