import patient
import staff
import doctor
import os


while True:
    os.system("cls")
    print("1. Staff Login\n2. Patient Login\n3. Doctor Login\n4. Exit")
    c = input("Enter number for choice : ")
    if c == "1":
        staff.staff_menu()
    elif c == "2":
        patient.login()
    elif c == "3":
        doctor.doctor_login()
    elif c == "4":
        break
    else:
        input("Unrecognised command (enter)")