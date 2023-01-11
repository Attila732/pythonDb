workerList=[]
def readFile(): 
    print("Beolvasás....")   
    
    file=open("employee.txt" , "r" , encoding="utf-8")
    row=file.readline()
    while(row):
        row=file.readline()
        rowSp=row.split(":")
        workerList.append(rowSp)
    print("Fájl beolvasva.\n")  
def countTaktaharkany():
    print("Taktaharkányi dolgozók")
    counter=0
    for worker in workerList:
        if(len(worker)!=1 and worker[2]=="Taktaharkány" ):
            counter+=1
    print("{} fő van Taktaharkányban".format(counter))
def MorahalomAverageSalary():
    print("Mórahalom átlag fizetése")
    sumSalary=0
    counter=0
    for worker in workerList:
        if(len(worker)!=1 and worker[2]=="Mórahalom"):
            salary=int(worker[4])
            sumSalary+=salary
            counter+=1
    Average=sumSalary/counter        
    print("Mórahalom átlag fizetés: {}".format(Average))

readFile()    
countTaktaharkany()
MorahalomAverageSalary()