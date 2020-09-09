51. In a given directory search all text files for the pattern "Treasure". 
       a) Find how many text file has the pattern.
       b) Count how many times pattern repeats in each file

  Note : Create at least 4 text file in a directory and keep the pattern in at least 2 files.
             Repeat the pattern in the file many times.
Ans:
import glob
import re
total = 0
for present in glob.glob("*.txt"):
    myfile = open(present, "r")
    strlist = myfile.read().split()
    for i in range(len(strlist)):
        string = re.sub(r'[?|$|.|!]',r'', strlist[i])
        strlist[i] = string
    if "Treasure" in strlist:
        print present, strlist.count("Treasure")
        total += strlist.count("Treasure")
    else:
        print present, 0
    myfile.close()
        
print "Total count:", total
