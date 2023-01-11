from emp import Employee

class Worker:
    def __init__(self):
        self.miner=Employee()
        self.engineer=Employee()
    def setEmployee(self):
        self.miner.name="Béla"
        self.miner.age=37
        self.miner.salary=750000
        self.engineer.name="Pali"
        self.engineer.age=34
        self.engineer.salary=540000
    def getEmployee(self):
        print("Bányász: ", self.miner.name)
        print("Mérnök: ", self.engineer.name)

work=Worker()
work.setEmployee()        
work.getEmployee()