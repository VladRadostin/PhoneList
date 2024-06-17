import GlobalScript

#interface
def interface():  

    print() 
    print("hello Uzer")
    print("use help to display commands")
    GlobalScript.Clear()



#interface command
def Command(command):
 
    match command:
        #command exit
        case 1:
            return

        #command Help
        case 2:
            print("help command\n")
            GlobalScript.HelpF()
            GlobalScript.Clear()

        #command Read File
        case 3:
            print("Read File command\n")
            GlobalScript.ReadF()
            GlobalScript.Clear()

        #command Record File
        case 4:
            print("Record File command\n")
            GlobalScript.RecordF()
            GlobalScript.Clear()

        #command Create data
        case 5:
            print("Create data command\n")
            GlobalScript.ChangesF()
            GlobalScript.Clear()

        #command Delete Data
        case 6:
            print("Delete Data command\n")
            GlobalScript.DeleteF()
            GlobalScript.Clear()

        #command Error
        case 0:
            print("           Error command            \ninvalid command: try to enter it again\n     use help to display commands     ")
            GlobalScript.Clear()


   