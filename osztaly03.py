class Harmadik:
    def __init__(self,numb1,numb2):
        self.szorzas=numb1*numb2
    def kiir(self):
        print(self.szorzas)
szorz=Harmadik(25,34)
szorz.kiir()                   
#konstruktorban nem csinalunk kritikus muveletet
class helyes:
    def __init__(self, num01,num02):  
        self.number01=num01
        self.number02=num02
    def multiply(self):
        result=self.number01*self.number02
        print(result)
szorz0=helyes(12,31)
szorz0.multiply()        
