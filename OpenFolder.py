import os

default_main_folder_path = 'C:/Users/USERNAME/Sermo/RealTime Pro Projects - Documents/'

def open_projects_folder(folder_name: str) -> None:
    main_folder_path = default_main_folder_path.replace('USERNAME', os.getlogin())
    
    if not os.path.exists(main_folder_path):
        main_folder_path = input("Enter the main folder path: ")
    
    
    if not folder_name.startswith("P30"):
        
        if folder_name.isdigit():
            if len(folder_name) == 6:
                folder_name = "P3" + folder_name
            elif len(folder_name) == 5:
                folder_name = "P30" + folder_name
            elif len(folder_name) == 4:
                folder_name = "P300" + folder_name

    folder_path = os.path.join(main_folder_path, folder_name)
    
    if os.path.exists(folder_path):
        os.startfile(folder_path)
    else:
        print(f"Folder '{folder_name}' not found at: {folder_path}")

# Get folder name from the user
folder_name = input("Enter the name of the folder: ")

open_projects_folder(folder_name)
