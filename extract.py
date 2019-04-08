import keywords

def extract(fileName):  #returns a map in form: num_of_line: [keyword1, keyword2]
    #####################initialization of variables##################
    #the dictionary that will be exported. Each pair will be in form: [(str)line_number : (str)[list_of_keywords_found]]
    Hmap = {}  
    #the current line number
    lineNum = 0

    allKW = keywords.allKW

    #open the target file and split the string into lines.
    file = open(fileName,"r")
    allText = file.read()
    splitted = allText.splitlines()

    #record all the 
    for line in splitted:
        lineNum += 1
        for word in allKW:
            if word in line:
                Hmap[str(lineNum)] = str(Hmap.get(str(lineNum))) + ", " + word

    #sort the list of keys into a list of ints.
    lineList = []
    for item in Hmap:
        lineList.append(int(item))

    #export into a file called "map.txt"
    # export = open("map.txt","w")
    # for i in sorted(lineList):
    #     export.write(str(i) + ": " + Hmap[str(i)] + "\n")
        


    #close all files to complete writing.        
    file.close()
    # export.close()
    return Hmap
# extract("./Grep.java")