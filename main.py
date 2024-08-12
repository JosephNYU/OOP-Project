from hospital_manager import HospitalManager
from utility import generate_random_data

if __name__ == '__main__':
    hospital = HospitalManager()
    generate_random_data(hospital)
    hospital.run()
