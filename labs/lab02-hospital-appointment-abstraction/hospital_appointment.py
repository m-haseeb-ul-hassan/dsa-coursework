########################################
# DSA - Lab 02                         #
# OOP (Abstraction & Encapsulation)    #
########################################

from abc import ABC, abstractmethod

# 1. Abstract Base Class

class Appointment(ABC):
    def __init__(self, appointment_id: int, patient_name: str):
        self._appointment_id = appointment_id
        self._patient_name = patient_name
        self._fee = 0.0
        self.__status = "Booked"

    @abstractmethod
    def calculate_fee(self):
        pass

    @abstractmethod
    def get_appointment_details(self):
        pass

    def get_status(self):
        return self.__status

    # 3. Encapsulation in Python
    def set_status(self, new_status):
        if new_status not in ["Booked", "Completed", "Cancelled"]:
            print(f"Invalid Status: {new_status}")
            return

        if self.__status == "Completed":
            print("Status can't be changed, it's already completed.")
            return

        self.__status = new_status
        print(f"Status updated to: {new_status}")


# 2. Concrete Classes (Abstraction in Python)

class GeneralAppointment(Appointment):
    def __init__(self, appointment_id: int, patient_name: str, doctor_name: str):
        super().__init__(appointment_id, patient_name)
        self._doctor_name = doctor_name
        self.calculate_fee()

    def calculate_fee(self):
        self._fee = 1500

    def get_appointment_details(self):
        print(f"Appointment ID: {self._appointment_id} \nPatient Name: {self._patient_name} "
              f"\nDoctor Name: {self._doctor_name} \nFee: {self._fee} PKR \nStatus: {self.get_status()}")


class SpecialistAppointment(Appointment):
    def __init__(self, appointment_id: int, patient_name: str, specialization: str, experience_years: int):
        super().__init__(appointment_id, patient_name)
        self._specialization = specialization
        self._experience_years = experience_years
        self.calculate_fee()

    def calculate_fee(self):
        self._fee = 1500 + (self._experience_years * 100)

    def get_appointment_details(self):
        print(f"Appointment ID: {self._appointment_id} \nPatient Name: {self._patient_name} "
              f"\nSpecialization: {self._specialization} \nExperience: {self._experience_years} years "
              f"\nFee: {self._fee} PKR \nStatus: {self.get_status()}")


# 4. Hospital Management Class

class Hospital:
    def __init__(self):
        self._appointments = []

    def add_appointment(self, appointment):
        self._appointments.append(appointment)
        print(f"Appointment added for {appointment._patient_name}")

    def show_all_appointments(self):
        print("All Appointments:")
        for appointment in self._appointments:
            appointment.get_appointment_details()
            print()

    def update_status(self, appointment_id, new_status):
        for appointment in self._appointments:
            if appointment._appointment_id == appointment_id:
                appointment.set_status(new_status)
                return
        print(f"Appointment ID {appointment_id} not found.")


# 5. Main Program (Simulation)

if __name__ == "__main__":
    hospital = Hospital()

    appt1 = GeneralAppointment(101, "Ali", "Dr. Ahmed")
    appt2 = GeneralAppointment(102, "Sara", "Dr. Fatima")

    appt3 = SpecialistAppointment(201, "Huzaifa", "Cardiology", 10)
    appt4 = SpecialistAppointment(202, "Ayesha Malik", "Neurology", 15)

    hospital.add_appointment(appt1)
    hospital.add_appointment(appt2)
    hospital.add_appointment(appt3)
    hospital.add_appointment(appt4)

    hospital.show_all_appointments()

    hospital.update_status(101, "Completed")
    hospital.update_status(201, "Cancelled")
    hospital.update_status(102, "Pending")
    hospital.update_status(101, "Cancelled")

    hospital.show_all_appointments()
