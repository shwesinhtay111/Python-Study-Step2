# open files programatically
# create file
f = open('practice.txt','w+')
f.write('test advance file folder')
f.close()

# Getting Directories
import os
os.getcwd()

# Listing Files in a Directory
print(os.listdir())

# In any directory you pass
print(os.listdir("C:\\Users"))

# Moving Files
# there are permission restrictions, for example if you are logged in a User A, you won't be able to make changes to the top level Users folder without the proper permissions
import shutil
# shutil.move('practice.txt','C:\\Users')
print(os.listdir())
# shutil.move('D:\Python Learning 2021\practice.txt',os.getcwd())

# Deleting Files
import send2trash
print(os.listdir())
send2trash.send2trash('practice.txt')
print(os.listdir())
os.getcwd()

#  "walk" through a directory
for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
        
    print('\n')
        
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
        
    # Now look at subfolders
