workerList=[]
def readFile(): 
    print("Beolvasás....")   
    
    file=open("dolgozok100.txt" , "r" , encoding="utf-8")
    row=file.readline()
    while(row):
        row=file.readline()
        rowSp=row.split(":")
        workerList.append(rowSp)
    print("Fájl beolvasva.\n")    
def countWorker():
    print("Dolgozók számolása.")
    counter=0
    for worker in workerList:
        if(len(worker)!=1 ):
            counter+=1
    print("{} fő dolgozó van".format(counter))        
def sumGyorSalary():
    print("Győri fizetések összege")
    sumSalary=0
    for worker in workerList:
        if(len(worker)!=1 and worker[1]=="Győr"):
            salary=int(worker[3])
            sumSalary+=salary
    print("Győri fizetések összege: {}".format(sumSalary))      
def SzolnokSalaryAverage():
    print("Szolnok fizetések átlaga")
    sumSalary=0
    counter=0
    for worker in workerList:
        if(len(worker)!=1 and worker[1]=="Szolnok"):
            salary=int(worker[3])
            sumSalary+=salary
            counter+=1
    Average=sumSalary/counter        
    print("Szolnoki fizetések átlaga: {}".format(Average))   
def countLajos():
    print("Lajosok számolása")
    counter=0
    for worker in workerList:
        if(len(worker)!=1 ):
            name=worker[0]
            nameSp=name.split(" ")
            if(nameSp[1]=="Lajos"):
                counter+=1
    print("A Lajosok száma: {}\n".format(counter))  
         

readFile()
countWorker()
sumGyorSalary()
SzolnokSalaryAverage()
countLajos()       

  

