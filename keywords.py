import keyword

pythonList = set(keyword.kwlist)
javaList = { "abstract","assert","boolean","break","byte","case","catch","char","class","const","continue","default","do","double","else","enum","extends","final","finally","float","for","goto","if","implements","import","instanceof","int","interface","long","native","new","package","private","protected","public","return","short","static","strictfp","super","switch","synchronized","this","throw","throws","transient","try","void","volatile","while" }
cList = {"auto","else","long","switch","break","enum","register","typedef","case","extern","return","union","char","float","short","unsigned","const","for","signed","void","continue","goto","sizeof","volatile","default","if","static","while","do","int","struct","_Packed","double"}






pythonList.union(javaList,cList)
allKW = list(pythonList)