from medical_department import MedicalDepartment
from utility import validate_input

class HospitalManager:
    def __init__(self):
        self.departments = []

    def print_menu(self):
        print("Program Options: ")
        options = [
            '1) Add new patients',
            '2) Print all patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            '5) End the program'
        ]
        print('\n'.join(options))
        prompt = f"Enter your choice from 1 to {len(options)} \n"
        return validate_input(prompt, 1, len(options))

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.print_all_patients()
            elif choice == 3:
                self.process_next_patient()
            elif choice == 4:
                self.remove_patient()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def add_patient(self):
        dept_name = input("Enter department: ")
        patient_name = input("Enter patient name: ")
        urgency_level = int(input("Enter urgency level (0 normal / 1 urgent / 2 super urgent) "))
        
        department = next((dept for dept in self.departments if dept.name == 'Department ' + dept_name), None)
        if department:
            department.add_new_patient(patient_name, urgency_level)
        else:
            new_dept = MedicalDepartment(dept_name)
            new_dept.add_new_patient(patient_name, urgency_level)
            self.departments.append(new_dept)

    def print_all_patients(self):
        for dept in self.departments:
            print(f'{dept.name}: There are {len(dept.patient_queue)} patients')
            dept.print_patients()

    def process_next_patient(self):
        dept_name = input("Enter department: ")
        department = next((dept for dept in self.departments if dept.name == 'Department ' + dept_name), None)
        if department:
            department.get_next_patient()
        else:
            print("There is no Department with this name")

    def remove_patient(self):
        dept_name = input("Enter department: ")
        patient_name = input("Enter patient name: ")
        department = next((dept for dept in self.departments if dept.name == 'Department ' + dept_name), None)
        if department:
            if department.remove_patient(patient_name):
                department.print_patients()
            else:
                print("No patient with such a name in this Department!")
        else:
            print("There is no Department with this name")
