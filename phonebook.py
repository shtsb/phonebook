def save():
    name = str (input ("please enter name"))
    phone = int (input ("please enter phone"))
    phonebook[name]=phone

def show():
    print(phonebook)

phonebook={}
while(True):
    choice=int(input("if you want enter new number enter 1 ,"
    " if you want to see all of numbers in phonebook enter 2 , if your numbers are finish enter 3"))
    if choice == 1 :
        save()
    elif choice == 2 :
        show()
    elif choice == 3 :
        show()
        break
    else :
        print("please choose beetween 1 ,2 ,3")

