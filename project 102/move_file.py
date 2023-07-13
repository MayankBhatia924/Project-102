import os
import shutil


downloads_folder = "C:/Users/Mayank/Downloads"
destination_folder = "C:/Users/Mayank/Desktop/Document_Files"


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


files = os.listdir(downloads_folder)


for file in files:
    
    _, file_extension = os.path.splitext(file)

    
    if not os.path.isdir(os.path.join(downloads_folder, file)):
        
        subfolder = os.path.join(destination_folder, file_extension[1:])  
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)

        
        shutil.move(os.path.join(downloads_folder, file), os.path.join(subfolder, file))

print("Files organized successfully!")
