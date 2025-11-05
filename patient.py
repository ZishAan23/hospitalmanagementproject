import os
import fileio

patients = fileio.read_file("patient_data.txt")
p=None

def order_meds():
    global p
    fileio.print_tabulated(p["prescription"])
    sern = int(input("Enter serial number of medicine to order: "))
    print("Select the site:\n1. Apollo\n2.Sasta Sundar\n")
    c = input("Enter number for choice : ")
    if c == "1":
        os.system("start https://www.apollopharmacy.in/search-medicines/"+p["prescription"][sern-1]["medicine"].replace(" ","%20"))
    elif c == "2":
        os.system("start https://sastasundar.com/search?q="+p["prescription"][sern-1]["medicine"].replace(" ","%20"))
    else:
        input("Unrecognised command (enter)")
        

def login():
    global patients
    global p
    while True:
        os.system("cls")
        print("1. Login\n2. Exit\n\n")
        c = input("Enter number for choice : ")
        if c == "1":
            id = int(input("Enter ID : "))
            for i in patients:
                if i["id"] == id:
                    p = i
                    patient_menu()
                    break
            else:
                input("Patient with id " + str(id) + " not found (enter)")
        elif c == "2":
            break
        else:
            input("Unrecognised command (enter)")

def patient_menu():
    global p
    while True:
        os.system("cls")
        print("1. View Data\n2. View Prescription\n3. Order From prescription\n4. Print prescription\n5. Exit\n\n")
        c = input("Enter number for choice : ")
        if c == "1":
            fileio.print_dict(p)
        elif c == "2":
            fileio.print_tabulated(p["prescription"])
        elif c == "3":
            order_meds()
        elif c == "4":
            path = input("Enter the path to dowload the excel sheet in : ")
            fileio.download_sheet_from_dict(p["prescription"], path)
        elif c == "5":
            break
        else:
            input("Unrecognised command (enter)")