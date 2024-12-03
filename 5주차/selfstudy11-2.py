inFp = None
inList, inStr =[], ""
num=1

inFp = open("C:/Temp/data1.txt","r",encoding="UTF-8")

inList = inFp.readlines()
for inStr in inList : 

    print("%d"%num + ": %s"%inStr)
    #rint(inStr, end="")
    num = num+1

inFp.close()