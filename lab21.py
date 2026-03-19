class Patient :
    def __init__(self, patient_number, patient_name, medical_card, private, num_days):
        self.number = patient_number
        self.name = patient_name
        self.medical_card = medical_card
        self.private = private
        self.num_days = num_days
        self.bill = 0
def set_stay(self, days):
    if num_day > 0:
        self.num_days = days
def set_length_of_stay(self, day):
    self.num_days = day
def get_name(self):
    return self.name
def calc_bill(self):
    if self.medical_card == "False":
        if self.private == "True":
            self.bill = self.num_days * 300
        else:
            self.bill = self.num_days * 100
    else:
        self.bill = 0
def Print(self):
    print("Name", self.name)
    print("Medical Card", self.medical_card)
    print("Private", self.private)
    print("Days In Hospital", self.num_days)
    print()
p1 = Patient("78922", "Jane Austin", "Yes", "Yes", 10)
p2 = Patient("67453", "Henry James", "No", "Yes", 5)

patient = input("Enter patient number: ")
name = input("Enter patient name: ")
medical_card = input("Enter (Y/N) if medical_card: ")
if medical_card == "Y" or medical_card == "y":
    medical_card = "Yes"
else:
    medical_card = "No"
private = input("Enter (Y/N) if private: ")
if private == "Y" or private == "y":
    private = "Yes"
else:
    private = "No"
num_day = int(input("Enter Number Of Days: "))

p3 = Patient(patient, name, medical_card, private, num_day)


print("*" * 25)
print("Patient Record")
print("*" * 25)
Print(p1)
calc_bill(p1)
print("*" * 25)
print("Patient Record")
print("*" * 25)
Print(p2)
calc_bill(p2)
print("*" * 25)
print("Patient Record")
print("*" * 25)
Print(p3)
calc_bill(p3)
set_stay(p2, 7)
print("*" * 25)
print("Patient Record")
print("*" * 25)
Print(p2)
calc_bill(p2)