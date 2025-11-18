import os
import random
import fileio
import population_graph
# made independently by me 

patients =[]
patient_dummy = {
	"id" : 0,
	"name" : "",
	"room": 0,
	"disease": "",
	"price": 0
}

doctors = []
doctor_dummy = {
	"id" : 0,
	"name" : "",
	"assigned to": 0
}


def view_p():
	os.system('cls')
	d = input("1. Search By Id\n2. Search by name\n\n\n")
	if d=="1":
		id = int(input("Enter id: "))
		f = None
		for p in patients:
			if p["id"] == id:
				f = p
				fileio.print_dict(p)
		if not f:
			input("Patient with id "+str(id)+" not found (enter)")

	if d == "2":
		name = input("Enter Name: ")
		f = None
		for p in patients:
			if p["name"] == name:
				f = p
				fileio.print_dict(p)
		if not f:
			input("Patient named "+str(name)+" not found (enter)")


def remove_p():
	os.system('cls')
	d = input("1. Remove By Id\n2. Remove by name\n\n\n")
	if d=="1":
		id = int(input("Enter id: "))
		f = None
		for p in patients:
			if p["id"] == id:
				f=p
				patients.remove(p)
		if not f:
			input("Patient with id "+str(id)+" not found (enter)")
		else:
			input("removed (enter)")
			
	if d == "2":
		name = input("Enter Name: ")
		f = None
		for p in patients:
			if p["name"] == name:
				f = p
				patients.remove(p)
		if not f:
			input("Patient named "+str(name)+" not found (enter)")
		else:
			input("removed (enter)")

def add_p():
	os.system('cls')
	p = patient_dummy.copy()
		
	p["name"] = input("Enter the name: ")
	p["room"] = int(input("Enter the room number: "))
	p["disease"] = input("Name of disease: ")
	p["id"] = random.randint(1,9999)
	
	input("Patient has been assigned the id : "+ str(p["id"])+ " (enter) ")
	patients.append(p)

def receipt():
	os.system("cls")
	d = int(input("Enter Id: "))
	found = None
	for p in patients:
		if p["id"] == d:
			os.system('cls')
			found = p
			fee = input("Enter the fees: ")
			p["price"] = fee
			print("\n\nName: ", p["name"])
			print("Disease: ", p["disease"])
			print("Doctor: ", p["doctor"])
			print("Charge: ", p["price"],"\n\n")
			input("(enter)")
	if not found:
		print("Not found")
		input("(enter)")

def patient_manage_menu():
	global patients
	while True:
		os.system('cls')
		print("1. View All \n2. View patient \n3. Add patient \n4. Remove Patient \n5. Get Receipt\n6. Exit\n\n")
		c = input("Enter the number for choice: ")
		
		patients = fileio.read_file("patient_data.txt")
		
		if c == "1":
			for d in patients:
				for i in d:
					print("\n",i, ": ", d[i])
				print("-"*10)
			input("(enter)")
		elif c == "2":
			view_p()
		elif c == "3":
			add_p()
		elif c == "4":
			remove_p()
		elif c == "5":
			receipt()
		elif c== "6":
			break
		else:
			input("unrecognised command (enter) ")
		
		fileio.write_file("patient_data.txt", patients)

		


def view_d():
	os.system('cls')
	d = input("1. Search By Id\n2. Search by name\n\n\n")
	if d=="1":
		id = int(input("Enter id: "))
		f = None
		for p in doctors:
			if p["id"] == id:
				f = p
				fileio.print_dict(p)
		if not f:
			input("Doctor with id "+str(id)+" not found (enter)")

	if d == "2":
		name = input("Enter Name: ")
		f = None
		for p in doctors:
			if p["name"] == name:
				f = p
				fileio.print_dict(p)
		if not f:
			input("Doctor named "+str(name)+" not found (enter)")


def remove_d():
	os.system('cls')
	d = input("1. Remove By Id\n2. Remove by name\n\n\n")
	if d=="1":
		id = int(input("Enter id: "))
		f = None
		for p in doctors:
			if p["id"] == id:
				f=p
				doctors.remove(p)
		if not f:
			input("Doctor with id "+str(id)+" not found (enter)")
		else:
			input("removed (enter)")
			
	if d == "2":
		name = input("Enter Name: ")
		f = None
		for p in doctors:
			if p["name"] == name:
				f = p
				doctors.remove(p)
		if not f:
			input("Doctor named "+str(name)+" not found (enter)")
		else:
			input("removed (enter)")

def add_d():
	os.system('cls')
	p = doctor_dummy.copy()
		
	p["name"] = input("Enter the name: ")
	p["assigned to"] = int(input("Enter the id of the assigned patient: "))
	p["id"] = random.randint(1,9999)
	j = p["assigned to"]
	pts = None
	for itm in patients:
		if itm["id"] == j:
			pts = itm
			break
		print(itm["id"])
	if not pts:
		input(f"There exists no patient with id {j}")
		return
	
	input("Doctor has been assigned the id : "+ str(p["id"])+ " (enter) ")
	doctors.append(p)

def assign_to():
	global patients
	global doctors

	i = int(input("Enter the id of the doctor: "))
	f = None
	for doctor in doctors:
		if doctor["id"] == i:
			f = doctor
			break
	if not f:
		input("Doctor with id "+str(i)+" not found (enter)")
	else:
		j = int(input("Enter the id of the patient to assign to: "))
		pts = None
		for itm in patients:
			if itm["id"] == j:
				pts = itm
				break
			print(itm["id"])
		if not pts:
			input(f"There exists no patient with id {j}")
			return
		
		f["assigned to"] = j
		input(f"Doctor {f['name']} has been assigned to patient {j} (enter)")
	

def doctor_manage_menu():
	global doctors
	global patients
	global doc
	global p

	while True:
		os.system('cls')
		print("1. View All Doctors \n2. View doctor \n3. Add doctor \n4. Remove doctor \n5. Assign to patient \n6. Exit\n\n")
		c = input("Enter the number for choice: ")
		
		doctors = fileio.read_file("doctor_data.txt")
		patients = fileio.read_file("patient_data.txt")
		
		if c == "1":
			for d in doctors:
				for i in d:
					print("\n",i, ": ", d[i])
				print("-"*10)
			input("(enter)")
		elif c == "2":
			view_d()
		elif c == "3":
			add_d()
		elif c == "4":
			remove_d()
		elif c== "5":
			assign_to()
		elif c == "6":
			break
		else:
			input("unrecognised command (enter) ")
		
		fileio.write_file("doctor_data.txt", doctors)
			
def staff_menu():
	while True:
		os.system("cls")
		print("1. Patient Management Menu\n2. Doctor Management Menu\n3. Graphs\n4. Exit\n\n")
		c = input("Enter the number for choice: ")

		if c=="1":
			patient_manage_menu()
		elif c=="2":
			doctor_manage_menu()
		elif c=="3":
			population_graph.plot_graph()
		elif c=="4":
			break
		else:

			input("unrecognised command (enter) ")
		
		population_graph.update_population()
