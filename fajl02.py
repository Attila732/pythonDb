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

readFile()
       

  
