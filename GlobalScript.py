import UI
import os
import Logger

clear = lambda: os.system('cls')


# command number - team number
def TeamNumbers(command):
    
    #command exit
    if command == "":
        return 1
        
    #command Help
    elif command == "Help" or command == "help":
        return 2

    #command Read File
    elif command == "Read File" or command ==  "read file":
        return 3

    #command Record File
    elif command == "Record File" or command ==  "record file":
        return 4

    #command Create data
    elif command == "Changes Data File" or command ==  "changes data file":
        return 5

    #command Delete Data
    elif command == "Delete Data File" or command == "delete data file":
        return 6

    #command Error
    else:
        return 0


# command number - team number programm
def TeamNumbersProgramm(tempCommandPO):

    file = None
    Datalist = []

    match tempCommandPO:
        case "2":
            print("uploading data \n")  
            
            Path_OS = os.path.join(os.getcwd(), "File")
            file = os.listdir(Path_OS)

            for i in range(len(file)):
                path = os.path.join("File\\", file[i])
                Datalist = Logger.Read(path)
                PrintList(Datalist, 2)
            
        case "3":
            file = FileSearch()
            print("uploading data \n")
            if file != 0:
                path = os.path.join("File\\", file)
                Datalist = Logger.Read(path)
                PrintList(Datalist, 2)

        case "4":
            file = FileSearch()
            print("create new data \n")
            if file != 0:
                path = os.path.join("File\\", file)
                Logger.Record(path)
        
        case "5":
            file = FileSearch()
            print("Changes data \n")
            if file != 0:
                path = os.path.join("File\\", file)
                Logger.Changes(path)

        case "6":
            file = FileSearch()
            print("delete data \n")
            if file != 0:
                path = os.path.join("File\\", file)
                Logger.Delete(path)
     



def Clear():

    # The exit line
    print()
    command = input("Press to exit: ")

    # clear
    clear()

    # Command return
    UI.Command(TeamNumbers(command))


def ReadF():
    clear()

    print("choose how to output files: 3 - output a specific file ; 2 - output all files ; 1 - exit\n")
    TempCommand = input("choose how to output files: ")

    clear()

    match TempCommand:
        case "1":
            return

        case "2":
            TeamNumbersProgramm(TempCommand)
            return

        case "3":
            TeamNumbersProgramm(TempCommand)
            return

    print("there is no such command\n")
    ReadF()
    

def RecordF():
    clear()

    print("select the command: 4 - writing to a file ; 1 - exit\n")
    TempCommand = input("select the command: ")

    clear()

    match TempCommand:
        case "1":
            return

        case "4":
            TeamNumbersProgramm(TempCommand)
            return

    print("there is no such command\n")
    RecordF()


def ChangesF():
    clear()

    print("select the command: 5 - Changes data ; 1 - exit\n")
    TempCommand = input("select the command: ")

    clear()

    match TempCommand:
        case "1":
            return

        case "5":
            TeamNumbersProgramm(TempCommand)
            return

    print("there is no such command\n")
    RecordF()


def DeleteF():
    clear()

    print("select the command: 6 - Delete data ; 1 - exit\n")
    TempCommand = input("select the command: ")

    clear()

    match TempCommand:
        case "1":
            return

        case "6":
            TeamNumbersProgramm(TempCommand)
            return

    print("there is no such command\n")
    RecordF()



# file search
def FileSearch():
    
    boolean = True
    path = os.path.join(os.getcwd(), "File")
    ListDir = os.listdir(path)

    PrintList(ListDir, 1)

    file = input("enter the file name: ")

    #clear
    clear()

    for i in range(len(ListDir)):
        if  file == ListDir[i]:
            boolean = False   

    if boolean:
        print("the file was not found or the file name was incorrect")
        return 0
    
    return file


# help list
def HelpF():
    HelpList = ["Command",
                "",
                "Read File          or  read file           - reads the file",
                "Record File        or  record file         - writing to a file",
                "Changes Data File  or  changes data file   - changes to the data in the file",
                "Delete Data File   or  delete data file    - deleting data in a file"
                ]
    
    PrintList(HelpList, 1)
    

# outputs data
# ComandSystem: 1 - service teams ; 2 - custom commands
def PrintList(List, ComandSystem):

    match ComandSystem:
        case 1:
            for i in range(len(List)):
                print(List[i])
            print("")

        case 2:
            j = 0
            string = ''
            for i in List:
                j += 1

                if j < 10:
                    temp1 = "0" + str(j)
                else:
                    temp1 = str(j)
                
                string += temp1 + ": " + str(i)
                
            
            
            print(string)
            
            


# checking for an invalid character
def AnUnavailableСharacter(Name, Surname, Phone, Address):
    string = Name + Surname + Phone + Address

    for i in range(len(string)):
        if string[i] == ";":
            return True
        
    return False

         