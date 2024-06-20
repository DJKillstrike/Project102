import os, shutil

#Create source path and destination path
from_dir = "C:/Users/aadit/OneDrive/Desktop/Project102/Downloads/"
to_dir = "C:/Users/aadit/OneDrive/Desktop/Project102/"

#List of files present in source path
list_of_files = os.listdir(from_dir)


#To print names of files in source path
print(list_of_files)

#Checking and moving files 
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf'] :
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files" + '/'
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        #Check if folder path exists before moving ELSE make new folder path then move
        if os.path.exists(path2):
            print('Moving '+ file_name + '.......')

            #Move file from path1 to path3
            shutil.move(path1, path3)
        else: 
            os.makedirs(path2)
            print('Moving '+ file_name + '.......')
            shutil.move(path1, path3)    


        




    
