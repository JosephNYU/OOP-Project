import tkinter as tk
from tkinter import ttk

# Sample data
patients = [
    {"name": "John Doe", "urgency": "High", "status": "Waiting"},
    {"name": "Jane Smith", "urgency": "Medium", "status": "In Treatment"},
    {"name": "Joseph Hwang", "urgency": "Low", "status": "In Treatment"}
]

class HospitalQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Patient Queue Management System")

        # main frame
        main_frame = ttk.Frame(self.root, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # patients list
        self.patient_listbox = tk.Listbox(main_frame, height=15)
        self.patient_listbox.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        for patient in patients:
            self.patient_listbox.insert(tk.END, patient["name"] + " - " + patient["urgency"])

        # details of patients
        self.details_label = ttk.Label(main_frame, text="Patient Details:")
        self.details_label.grid(column=1, row=0, sticky=tk.W)
        self.details_text = ttk.Label(main_frame, text="", relief=tk.SUNKEN)
        self.details_text.grid(column=1, row=1, sticky=(tk.W, tk.E))

        # queue management buttons
        add_button = ttk.Button(main_frame, text="Add Patient", command=self.add_patient)
        add_button.grid(column=0, row=2, sticky=tk.W)
        remove_button = ttk.Button(main_frame, text="Remove Patient", command=self.remove_patient)
        remove_button.grid(column=0, row=3, sticky=tk.W)

        # update patient details when button is selected
        self.patient_listbox.bind("<<ListboxSelect>>", self.show_details)

    def add_patient(self):
        # add patient
        print("Adding a patient...")

    def remove_patient(self):
        # remove patient
        selections = self.patient_listbox.curselection()
        if selections:
            self.patient_listbox.delete(selections[0])
            print("Patient removed.")

    def show_details(self, event):
        # display selected patient's details
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            patient = patients[index]
            details = f"Name: {patient['name']}\nUrgency: {patient['urgency']}\nStatus: {patient['status']}"
            self.details_text.config(text=details)

def main():
    root = tk.Tk()
    app = HospitalQueueApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
