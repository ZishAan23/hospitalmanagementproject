import fileio
import os

ds = fileio.read_file("doctor_data.txt")
ps = fileio.read_file("patient_data.txt")
p = None
doc = None


def doctor_login():
    global ds
    global ps
    global p
    global doc

    while True:
        ds = fileio.read_file("doctor_data.txt")
        ps = fileio.read_file("patient_data.txt")

        os.system("cls")
        print("1. Enter ID For Login\n2. Exit\n\n")
        c = input("Enter number for choice : ")
        if c == "1":
            id = int(input("Enter ID : "))
            doc = None
            for d in ds:
                if d["id"] == id:
                    doc = d
                    doctor_menu(d)     
            if not doc:
                input("Doctor with id " + str(id) + " not found (enter)")
            else:
                for i in ps:
                    if i["id"] == doc["assigned to"]:
                        p = i
                        break
        elif c == "2":
            break
        else:
            input("Unrecognised command (enter)")
        
        

def create_prescription():
    
    prs = []
    prs_dummy = {
        "medicine": "",
        "dosage": "",
        "remarks": "",
        "price": 0
    }
    global p

    if not p:
        input("No patient assigned to this doctor (enter)")
        return

    while True:
        os.system("cls")
        fileio.print_tabulated(prs)
        print()
        print("1. Add Medicine\n2. Edit Entry\n3. Exit\n\n")
        c = input("Enter number for choice : ")
        if c == "1":
            i = prs_dummy.copy()
            i["medicine"] = input("Enter medicine name ")
            i["dosage"] = input("Enter dosage ")
            i["remarks"] = input("Enter remarks ")
            i["price"] = int(input("Enter price "))
            prs.append(i)
            input("Medicine added (enter)")
            
        elif c == "2":
            i = int(input("Enter serial no of entry to edit : "))
            prs[i-1]["medicine"] = input("Enter medicine name ")
            prs[i-1]["dosage"] = input("Enter dosage ")
            prs[i-1]["remarks"] = input("Enter remarks ")
            prs[i-1]["price"] = int(input("Enter price "))
            input("Medicine edited (enter)")
            
        elif c == "3":
            break
        else:
            input("Unrecognised command (enter)")
        p["prescription"] = prs

def generate_bill():
    global p
    total = 0
    if not p:
        input("No patient assigned to this doctor (enter)")
        return

    if p["prescription"]:
        for i in p["prescription"]:
            total += i["price"]
        p["price"] = total
    else:
        pr = int(input("Enter Price: "))
        p["price"] = pr
        return
    
    print(f"Bill generated for {p['name']}, total charge: {p['price']} (enter)")

    should_p = input("Should generate a excel file (yes or no) : ")
    if should_p.lower() == "yes":
        path = input("Enter the path to download the bill sheet: ")
        fileio.download_sheet_from_dict(p["prescription"] , path)
        input("Bill downloaded (enter)")
    else:
        input("price calculated (enter)")


def doctor_menu(d):
    global ds
    global ps
    global p

    ds = fileio.read_file("doctor_data.txt")
    ps = fileio.read_file("patient_data.txt")


    for i in ps:
        if i["id"] == d["assigned to"]:
            p = i
            break
    
    while True:
        os.system("cls")
        print("1. View Patient\n2. Create Prescription\n3. Generate Bill\n4. Exit\n\n")
        c = input("Enter number for choice : ")
        if c == "1":
            for i in ps:
                if i["id"] == d["assigned to"]:
                    fileio.print_dict(i)
                    break
            else:
                input("No patients assigned to this doctor (enter)")
        
        elif c == "2":
            create_prescription()
        elif c == "3":
            generate_bill()
        elif c == "4":
            break
        else:
            input("Unrecognised command (enter)")
        
        fileio.write_file("patient_data.txt", ps)