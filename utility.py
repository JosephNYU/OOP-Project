from medical_department import MedicalDepartment

def validate_input(prompt, start=0, end=None):
    while True:
        user_input = input(prompt)
        if not user_input.isdecimal():
            print("Invalid input. Try again!")
        elif start is not None and end is not None:
            if not (start <= int(user_input) <= end):
                print("Invalid range. Try again!")
            else:
                return int(user_input)
        else:
            return int(user_input)

def generate_random_data(hospital_manager):
    import random
    for i in range(1, 6):
        new_department = MedicalDepartment(str(i))
        for j in range(6):
            dummy_name = f'dummy {j}'
            new_department.add_new_patient(dummy_name, random.randint(0, 2))
        hospital_manager.departments.append(new_department)
