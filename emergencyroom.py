import heapq
import random

class EmergencyRoom:
    def __init__(self):
        self.patients_queue = []
        heapq.heapify(self.patients_queue)

    def add_patient(self, patient_name, priority):
        heapq.heappush(self.patients_queue, (priority, patient_name))

    def treat_patients(self):
        while self.patients_queue:
            priority, patient_name = heapq.heappop(self.patients_queue)
            print(f"Treating patient: {patient_name} (Priority: {priority})")

# Initialize the emergency room
emergency_room = EmergencyRoom()

# Generate random patients data
patients_data = [
    ("Saumya", random.randint(1, 5)),
    ("Maazin", random.randint(1, 5)),
    ("Sara", random.randint(1, 5)),
    ("Andrew", random.randint(1, 5))
]

print("Patients arriving at the Emergency Room:")
for patient_name, priority in patients_data:
    print(f"Patient: {patient_name} (Priority: {priority})")
    emergency_room.add_patient(patient_name, priority)

print("\nTreating patients based on priority:")
emergency_room.treat_patients()
