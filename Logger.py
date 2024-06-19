import GlobalScript
from DateCreate import Name_date, Surname_date, Phone_date, Address_date


def Read(Path): 

    TempDataList = []

    print(Path)

    with open(Path, 'r', encoding='utf-8') as f:
        DataList = f.readlines()
        TempDataList = DataList

    return TempDataList



def Record(Path):

    print("enter the data without the symbol ;\n")
    
    name = Name_date()
    Surname = Surname_date()
    Phone = Phone_date()
    Address = Address_date()

    ErrorСharacter = GlobalScript.AnUnavailableСharacter(name, Surname, Phone, Address)

    if ErrorСharacter == True:
        print("an invalid character is used ;")
        input("Press enter to continue: ")
        GlobalScript.RecordF()
        return


    Bollformatfile = FormatFile(Path)

    if Bollformatfile:
        with open(Path, 'a', encoding='utf-8') as f:
            f.write(f"{name};{Surname};{Phone};{Address}\n\n")
    else:
        with open(Path, 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{Surname}\n{Phone}\n{Address}\n\n") 



def Changes(Path):
    
    
    colim = int(input("which columns should the data be changed in: "))
    
    Bollformatfile = FormatFile(Path)

    TempDataList = []
    
    if Bollformatfile:

        name = Name_date()
        Surname = Surname_date()
        Phone = Phone_date()
        Address = Address_date()

        string = f"{name};{Surname};{Phone};{Address};"
            
        with open(Path, 'r', encoding='utf-8') as f:
            DataList = f.readlines()
            TempDataList = DataList

        TempDataList[colim - 1] = string + "\n"

        with open(Path, 'w', encoding='utf-8') as f:
            f.writelines(TempDataList)

    else:
        temp1 = ""
        tempComand = int(input("which data should be replaced 1 - name ; 2 - survase ; 3 - phone; 4 - adress : "))
        print("enter the data without the symbol ;\n")

        match tempComand:
            case 1:
                name = Name_date()
                temp1 = name

            case 2:
                Surname = Surname_date()
                temp1 = Surname

            case 3:
                Phone = Phone_date()
                temp1 = Phone
            
            case 4:
                Address = Address_date()
                temp1 = Address

        ErrorСharacter = GlobalScript.AnUnavailableСharacter(temp1, temp1, temp1, temp1)

        if ErrorСharacter == True:
            print("an invalid character is used ;")
            input("Press enter to continue: ")
            GlobalScript.ChangesF()
            return

        with open(Path, 'r', encoding='utf-8') as f:
            DataList = f.readlines()
            TempDataList = DataList

        TempDataList[colim - 1] = temp1 + "\n"

        with open(Path, 'w', encoding='utf-8') as f:
            f.writelines(TempDataList)



def Delete(Path):

    colim = int(input("enter the row of data that you want to delete: "))
    

    Bollformatfile = FormatFile(Path)

    delete = "\n"
    TempDataList = []
    
    if Bollformatfile:
        
        with open(Path, 'r', encoding='utf-8') as f:
            DataList = f.readlines()
            TempDataList = DataList

        TempDataList[colim - 1] = delete

        with open(Path, 'w', encoding='utf-8') as f:
            f.writelines(TempDataList)

    else:
        with open(Path, 'r', encoding='utf-8') as f:
            DataList = f.readlines()
            TempDataList = DataList

        TempDataList[colim - 1] = delete

        with open(Path, 'w', encoding='utf-8') as f:
            f.writelines(TempDataList)



def FormatFile(Path):

    string = ''
    trea = []

    with open(Path, 'r', encoding='utf-8') as f:
        DataList = f.readlines()
        trea = DataList
    
    for i in trea:
        string += str(i)

    print(string)
    for i in range(len(string)):
        if string[i] == ";":
            return True

    return False

