from pathlib import Path
import shutil
import os

def create_folder():
    try:
        name=input("Please tell your folder name: ")
        p=Path(name)
        p.mkdir()
        print("Folder Created Successfully")
    except Exception as err:
        print("Sorry an error occured while creating a folder")
        # print(err)

def read_file_folder():

    p=Path("")
    items=list(p.rglob('*'))
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")


def update_folder():
    try:
        read_file_folder()
        old_name=input("please tell which folder you want to update: ")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("please tell new name for your folder: ")
            new_p=Path(new_name) 
            p.rename(new_p)
            print("Your folder name is updated successfully")
        else:
            print("Sorry no such folder exists")
    except Exception as err:
        print(f"Error occured while changing the folder name {err}")


def delete_folder():
    try:
        read_file_folder()
        name=input("please tell which folder you want to delete: ")
        p=Path(name)
        if p.exists() and p.is_dir():
            #p.rmdir() #THis is used to delete a folder if folder is empty
            shutil.rmtree(p) #THis is used to delete a folder recursively means even if it contains a file or folder,it will also get deleted
            print("Folder deleted successfully")
        else:
            print("No such folder exists")
    except Exception as err:
        print(f"An error occured while deleting the folder {err}")


def create_file():
    try:
        read_file_folder()
        name=input("please tell your file name: ")
        p=Path(name)
        if not p.exists():
            with open(p,"x") as fs:#OR use name instead of p
                data=input("Write what you want in this file: ")
                fs.write(data)
            print("File created Successfully")

        else:
             print("File already exists")  
    except Exception as err:
        print(f"An error occured as {err}") 
           
def read_file():
    try:
        read_file_folder()
        name=input("Please tell the file name you want to read: ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:#OR use name instead of p
                content=fs.read()
                print(f"Your File content is : \n{content}")

        else:
            print("No such file exist ")
    except Exception as err:
        print(f"An error occured as {err}")


def update_file():
    try:
        read_file_folder()
        name=input("Please tell the file name you want to update: ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Options")
            print("1.For renaming the file")
            print("2.For appending something in the file")
            print("3.For overwriting the file content")
            choice=int(input("Tell Your choice: "))

            if choice==1:
                new_name=input("Enter the new name for the file with extension: ")
                new_p=Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("File name changed successfully")
                else:
                    print("File name already Exist")

            if choice==2:
                with open(name,"a") as fs:
                    content=input("Add whatever you want to append to the file")
                    fs.write(" "+content)
                print("Your content is appended to the file successfully")

            if choice==3:
                with open(name,"w") as fs:
                    content=input("Add whatever you want to add to the file to overwrite it")
                    fs.write(" "+content)
                print("Data changed successfully")
    except Exception as err:
        print(f"An error occured as {err}")


def delete_file():
    try:
        read_file_folder()
        name=input("Please tell the file name you want to delete: ")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")

while True:
    print("Options : -")


    print("1. Create a folder")
    print("2. Read files and folder")
    print("3. Update the folder")
    print("4. Delete the folder")
    print("5. Create a file")
    print("6. Read a file")
    print("7. Update the file")
    print("8. Delete the file")
    print("Press 0 to exit")

    choice=int(input("Please choose your option\n"))

    if choice==1:
        create_folder()
    if choice==2:
        read_file_folder()
    if choice==3:
        update_folder()
    if choice==4:
        delete_folder()
    if choice==5:
        create_file()
    if choice==6:
        read_file()
    if choice==7:
        update_file()
    if choice==8:
        delete_file()
    if choice==0:
        print("Thank you for visiting")
        break