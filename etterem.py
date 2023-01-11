from dolgozok import Employee

class Worker:
    def __init__(self):
        self.szakacs=Employee()
        self.pincer=Employee()
    def setEmployee(self):
        self.szakacs.name="Kristóf"
        self.szakacs.age=37
        self.szakacs.salary=900000
        

        self.pincer.name="Bálint"
        self.pincer.age=34
        self.pincer.salary=440000
        

    def getEmployee(self):
        print("Szakács: ", self.szakacs.name,"\nÉletkora: ",self.szakacs.age,"\nKeresete: ",self.szakacs.salary,"\nMi a dolga: ")
        print("Szakács: ")
        self.szakacs.working("Főz")
        print("\n")
        print("Pincér: ", self.pincer.name,"\nÉletkora: ",self.pincer.age,"\nKeresete: ",self.pincer.salary,"\nMi a dolga: ")
        
        print("Pincér: ")
        self.pincer.working("Felszolgál")

work=Worker()
work.setEmployee()        
work.getEmployee()
