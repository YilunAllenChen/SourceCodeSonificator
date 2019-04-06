file = open("./test.java","r")
allText = file.read()
#line = file.readline()

allText.split("\n")

print(allText[1])
file.close()