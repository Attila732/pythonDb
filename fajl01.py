def readFile():    
    workerList=[]
    file=open("dolgozok100.txt" , "r" , encoding="utf-8")
    row=file.readline()
    while(row):
        row=file.readline()
        rowSp=row.split(":")
        workerList.append(rowSp)
    print("Fájl beolvasva.")    
readFile()    





