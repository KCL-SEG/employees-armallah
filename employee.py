"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType,  **kwargs):
        self.name = name
        if contractType.upper() == "MONTHLY":
            self.contract= salaryContract(name, **kwargs)
        else:
            self.contract = hourlyContract(name, **kwargs)
        
    def get_pay(self):
        return self.contract.calculateMonthlyPay()

    def __str__(self):
        return self.contract.printPayDesc()
    
 
class salaryContract(Employee):
    def __init__(self, name,  **kwargs):
        self.name = name
        self.monthlySalary = kwargs.get("monthlySalary",0)
        self.comission = kwargs.get("comission",0)
        self.comissionedContracts = kwargs.get("comissionedContracts",0)
    def calculateMonthlyPay(self):
        if (self.comission != 0 and self.comissionedContracts == 0):
            return self.monthlySalary + self.comission
        return self.monthlySalary + self.comission * self.comissionedContracts
    def printPayDesc(self):
        string = f"{self.name} works on a monthly salary of {self.monthlySalary} "
        if self.comissionedContracts != 0:
            string += f"and recieves a comission for {self.comissionedContracts} at {self.comission} contract. "
        elif self.comissionedContracts == 0 and self.comission != 0:
            string += f"and receives a bonus comisison of {self.comission}. "
        string += f"Their total pay is {self.calculateMonthlyPay()}. "
        return string
    
class hourlyContract(Employee):
    def __init__(self,name,  **kwargs):
        self.name = name
        self.contractLength = kwargs.get("contractLength",0)
        self.hourlyPay = kwargs.get("hourlyPay",0)
        self.comission = kwargs.get("comission",0)
        self.comissionedContracts = kwargs.get("comissionedContracts",0)
    def calculateMonthlyPay(self):
        if (self.comission != 0 and self.comissionedContracts == 0):
            return self.contractLength * self.hourlyPay + self.comission
        return self.contractLength * self.hourlyPay + self.comission * self.comissionedContracts
    def printPayDesc(self):
        string = f"{self.name} works on a contract of {self.contractLength} at {self.hourlyPay} hour "
        if self.comissionedContracts != 0:
            string += f"and recieves a comission for {self.comissionedContracts} at {self.comission} contract. "
        elif self.comissionedContracts == 0 and self.comission != 0:
            string += f"and receives a bonus comisison of {self.comission}. "
        string += f"Their total pay is {self.calculateMonthlyPay()}"
        return string

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"monthly", monthlySalary = 4000)
print(billie.get_pay())
print(str(billie))
#Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "contract" ,contractLength=100, hourlyPay=25)
print(charlie.get_pay())
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", monthlySalary=3000, comission=4, comissionedContracts=200)
print(renee.get_pay())
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", contractLength=150, hourlyPay=25, comission=220, comissionedContracts=3)
print(jan.get_pay())
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly",monthlySalary=2000, comission=1500)
print(robbie.get_pay())
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "contract", contractLength=120, hourlyPay=30, comission=600)
print(ariel.get_pay())
print(str(ariel))