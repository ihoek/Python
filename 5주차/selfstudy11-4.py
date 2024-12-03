inFp, outFp = None, None
inStr = ""
fName = ""

fName = input("소스 파일명을 입력하시오 : ")
tName = input("타킷 파일명을 입력하시오 : ")

inFp = open(fName,"r")
outFp = open(tName,"w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--정상적으로 파일에 씀--")