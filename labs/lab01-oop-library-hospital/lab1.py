###########################################
# Question 1 : Library Management System  #
###########################################

class LibraryItem:
    def __init__(self,  item_title: str, item_ID: float):
        self.item_title = item_title
        self.item_ID    = item_ID
        self.avalibility_status = True
    
    def borrow_Item (self):
        if self.avalibility_status == True:
            self.avalibility_status = False
            print(f"You have borrwoed: {self.item_title} \nThanks ")
        else:
            print (f"{self.item_title} is not available. Thanks")
    
    def return_Item (self):
        if self.avalibility_status == False:
            self.avalibility_status = True
            print (f"You have returned:{self.item_title} \nThanks")
        else:
            print (f"{self.item_title} was not borrowed. \nThanks")
    
    def display_status(self):
        status = "Available" if self.avalibility_status else "Not Available"
        print(f"{self.item_title} is currently: {status}")
    
class Book (LibraryItem):
    def __init__(self, item_title: str, item_ID: float , author: str, no_of_Pages :int):
        super().__init__(item_title , item_ID)
        self.author = author
        self.no_of_pages  = no_of_Pages
    
    def display_detailed_information(self):
        status = "Available" if self.avalibility_status else "Not Available"
        print("Book Detailed Information")
        print(f"The {self.item_title} Book is written by {self.author}, has {self.no_of_pages} number of pages and it's ID is {self.item_ID} is currently {status} in Library.")

book1 = Book("Intro to Python", "00111", "Hassan", 500)
book1.display_detailed_information()
book1.borrow_Item()
book1.display_detailed_information()
book1.return_Item()
book1.display_detailed_information()


###########################################
# Question 2: Hospital Management System  #
###########################################

class Person:
    def __init__(self, person_ID: int, name: str, age: int):
        self.person_ID = person_ID
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"ID: {self.person_ID}, Name: {self.name}, Age: {self.age}")


class Patient(Person):
    def __init__(self, patient_ID: int, name: str, age: int):
        super().__init__(patient_ID, name, age)
        self.patient_ID = patient_ID
        self.appointments = []

    def add_appointments(self, appointment):
        self.appointments.append(appointment)
    
    def remove_appointment(self, appointment):
        if appointment in self.appointments:
            self.appointments.remove(appointment)

    def list_appointments(self):
        print(f"\nAppointments for {self.name}:")
        if len(self.appointments) == 0:
            print("No appointments")
        else:
            for appointment in self.appointments:
                print(f"Appointment ID: {appointment.appointment_id}, Date: {appointment.date}")


class Doctor(Person):
    def __init__(self, doctor_ID: int, name: str, age: int, specialization: str):
        super().__init__(doctor_ID, name, age)
        self.doctor_ID = doctor_ID
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
    
    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
    
    def list_patients(self):
        print(f"\nPatients under Dr. {self.name}:")
        if len(self.patients) == 0:
            print("No patients")
        else:
            for patient in self.patients:
                print(f" Patient Name is {patient.name} and ID: {patient.patient_ID}")


class Appointment:
    def __init__(self, appointment_ID: int, patient, doctor, date: str):
        self.appointment_id = appointment_ID
        self.patient = patient
        self.doctor = doctor
        self.date = date
    
    def details(self):
        print(f"\nAppointment Details:")
        print(f" Appointment ID: {self.appointment_id} \n Patient: {self.patient.name} \n Doctor: Dr. {self.doctor.name} \nSpecialization: {self.doctor.specialization} \nDate: {self.date}")


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
    
    def register_patient(self, patient):
        self.patients.append(patient)
        print(f"{patient.name} has been registered successfully.")
    
    def list_patients(self):
        print("Patients:")
        for p in self.patients:
            print(f" {p.patient_ID}  {p.name} Age: {p.age}")
    
    def list_doctors(self):
        print("Doctors:")
        for d in self.doctors:
            print(f"  {d.doctor_ID}  Dr. {d.name}, {d.specialization}")
    
    def list_appointments(self):
        print("Appointments:")
        for a in self.appointments:
            print(f"  {a.appointment_id}  {a.patient.name} with Dr. {a.doctor.name} on {a.date}")


hospital = Hospital()

p1 = Patient(10111, "Ali", 19)
p2 = Patient(10222, "Mustafa", 18)
hospital.register_patient(p1)
hospital.register_patient(p2)


d1 = Doctor(201, "Hassan", 35, "Cardiology")
hospital.doctors.append(d1)


apt1 = Appointment(301, p1, d1, "2025-02-02")
hospital.appointments.append(apt1)
p1.add_appointments(apt1)
d1.add_patient(p1)


hospital.list_patients()
hospital.list_doctors()
hospital.list_appointments()
