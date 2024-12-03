outFp = None
outStr = ""
fName = ""

fName = input("파일명을 입력하시오 : ")

outFp = open("C:/Temp/"+fName+".txt","w")

while True :
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break

outFp.close()
print("--정상적으로 파일에 씀--")