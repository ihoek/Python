inFp, outFp = None, None
inStr = ""

inFp = open("C:/windows/win.ini","r")
outFp = open("C:/Temp/data3.txt","w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--정상적으로 파일에 씀--")