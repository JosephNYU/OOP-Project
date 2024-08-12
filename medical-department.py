from patient import *

class MedicalDepartment:
    MAX_CAPACITY = 10
    PATIENT_URGENCY_LEVELS = [0, 1, 2]

    def __init__(self, name):
        self.name = 'Department ' + name
        self.patient_queue = []

    def add_new_patient(self, name, urgency_level):
        if len(self.patient_queue) >= self.MAX_CAPACITY:
            print("Apologies, the queue is full for this department.")
            return
        if urgency_level not in self.PATIENT_URGENCY_LEVELS:
            print("Invalid urgency level. Level should be 0 (normal), 1 (urgent), or 2 (super-urgent).")
            return
        new_patient = Patient(name, urgency_level)
        self.patient_queue.append(new_patient)
        self.patient_queue.sort(key=lambda x: x.urgency_level, reverse=True)
        print(f"Patient: {new_patient.name} is {self.format_patient_urgency(new_patient.urgency_level)}")

    def get_next_patient(self):
        if len(self.patient_queue) == 0:
            print("The Queue is empty")
            return
        next_patient = self.patient_queue.pop(0)
        print(f"{next_patient.name}, Please go with the Dr")

    def remove_patient(self, name):
        patients_to_remove = [patient for patient in self.patient_queue if patient.name == name]
        for patient in patients_to_remove:
            self.patient_queue.remove(patient)
        return len(patients_to_remove) > 0

    def print_patients(self):
        for patient in self.patient_queue:
            print(f"Patient: {patient.name} is {self.format_patient_urgency(patient.urgency_level)}")

    def is_full(self):
        return len(self.patient_queue) >= self.MAX_CAPACITY

    def __str__(self):
        return f"{self.name}: There are {len(self.patient_queue)} patients"

    @staticmethod
    def format_patient_urgency(urgency_level):
        if urgency_level == 0:
            return "Normal"
        elif urgency_level == 1:
            return "Urgent"
        return "Super-Urgent"
