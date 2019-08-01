infile = "ToDo.txt" # replace with path to your ToDo.txt
# The file will be in the same directory as the Python program

# read in ToDo.txt here using readlines
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
  
# create empty dictionary to store data as we loop
task_dict = {}

for line in lines:
   linelist=line.strip().split(",")
   task = linelist[0] #split the line and pull out task by index
   priority = linelist[1] #split the line and pull out priority by index
   task_dict[task]=priority # add line to add new key to a dictionary here using task ask key and priority as value

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    strChoice = strChoice.strip()
    print()#adding a new line

    # Choice 1 -Show the current items in the table
    if (strChoice == '1'):
        for nkey, nvalue in task_dict.items():
            print(nkey + ',' + nvalue) # loop through the dictionary here and print items
    
    # Choice 2 - Add a new item to the list/Table
    elif(strChoice == '2'):
        nkey=input("Enter new task:")
        nvalue=input("Enter task priority (high/low):")
        task_dict[nkey] = nvalue  # add a new key, value pair to the dictionary
   
    # Choice 3 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        if remove_key in task_dict:
            del task_dict[remove_key] # locate key and delete it using del function

    # Choice 4 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        with open(infile, 'w') as todo_file: # open a file handle
            for nkey, nvalue in task_dict.items():
                todo_file.write(nkey +','+ nvalue + '\n')
                # loop through key, value and write to file
    
    # Chocie 5- end the program
    elif (strChoice == '5'):
        break #and Exit the program
