inFp = None
inList = ""

inFp = open("C:/Temp/data1.txt","r",encoding="UTF-8")

inList = inFp.readlines()
print(inList)

inFp.close()