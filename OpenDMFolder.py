import os

# Define default main folder path
default_main_folder_path = 'C:/Users/USERNAME/Sermo/RealTime Pro Projects - Documents/'

# Function to open projects folder
def open_projects_folder(folder_name: str) -> None:
    # Replace USERNAME with the actual user name
    main_folder_path = default_main_folder_path.replace('USERNAME', os.getlogin())
    
    # Check if the main folder path exists, if not, ask the user to provide it
    if not os.path.exists(main_folder_path):
        main_folder_path = input("Enter the main folder path: ")
    
    # Check if the provided folder name starts with "P30"
    if not folder_name.startswith("P30"):
        # Adjust the folder name based on the number of digits provided
        if folder_name.isdigit():
            if len(folder_name) == 6:
                folder_name = "P3" + folder_name
            elif len(folder_name) == 5:
                folder_name = "P30" + folder_name
            elif len(folder_name) == 4:
                folder_name = "P300" + folder_name

    folder_path = os.path.join(main_folder_path, folder_name)
    
    if os.path.exists(folder_path):
        #print(folder_path)
        
        folder_path2 = folder_path + '/07 Survey Data Operations/b Scripts/'
        # List all files in the folder
        
        if os.path.exists(folder_path2):
            os.startfile(folder_path2)
            
            files = os.listdir(folder_path2)
            # Check each file for the text "Delivery Manager" in its name
            for file_name in files:
                if "Delivery_manager" in file_name:
                    # If found, construct the full file path and open it
                    file_path = os.path.join(folder_path2, file_name)
                    os.startfile(file_path)
                    return  # Exit the function after opening the file
            print("No Excel file with 'Delivery Manager' text found.")
        else:
           os.startfile(folder_path) 
    else:
        print(f"Folder '{folder_name}' not found at: {folder_path}")

# Get folder name from the user
folder_name = input("Enter the name of the folder: ")

# Call the function to open the specified folder
open_projects_folder(folder_name)
