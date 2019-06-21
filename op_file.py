import os


print("What you want to do:")
print("Press 1 : Create New File")
print("Press 2 : Open Existing File_ReadOnly")
print("Press 3 : Edit in file")
print("Press 4 : Delete a file")
print("Press 5 : Dispaly all files")

op = int(input("Enter Your Preferred Option:"))

if op ==1:
    cr_file = input("Enter File Name:")
    content = input("Enter Your Content Here:")
    with open(cr_file,"x") as nfile:
      new = nfile.write(content)
    print("Your contents are saved...")
    print(new)

elif op==2:
    print("Your current directory contains following files")
    pd = os.getcwd()
    f = []
    for r, d, f in os.walk(pd):
        for file in f:
            print(file)

    selected_file = input("Please enter your file name to open...:")
    with open(selected_file) as sfile:
      data = sfile.read()
      print(data)
elif op==3:
    print("Which file you want to edit...:")
    pd = os.getcwd()
    f = []
    for r, d, f in os.walk(pd):
        for file in f:
            print(file)

    selected_file = input("please enter your file name to edit...:")
    with open(selected_file,"a") as sfile:
     # data = sfile.read()
     # print(data)
      sfile.seek(0)
      update = input("Now you can edit here...pls edit here: ")
      data = sfile.write(update)

elif op==4:
    print("you have following files in your directory...")
    pd = os.getcwd()
    f = []
    for r, d, f in os.walk(pd):
        for file in f:
            print(file)

    delete_file = input("enter file to delete:")
        
      
    if os.path.exists(delete_file):
        os.remove(delete_file)
    else:
        print("Your given filename does not exist!")      

elif op==5:
    print("you have following files in your current directory....")
    pd = os.getcwd()
    f = []
    for r, d, f in os.walk(pd):
        for file in f:
            print(file)
else:
    print("Invalid option selected....")





