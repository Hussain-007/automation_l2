49. Write a program to perform  following file operations
a) Open the file in read mode and read all its contents on to STDOUT.
b) Open the file in write mode and enter 5 new lines of strings in to the new file.
c) Open file in Append mode and add 5 lines of text into it.
Ans:
myfile = open("output.txt", "r")
print myfile.read()
myfile.close()

myfile = open("sample.txt", "w")
myfile.write("My name is Pranav")
myfile.write("working on python")
myfile.write("to enhance my skills")
myfile.write("Saturday is a holiday")
myfile.write("Sunday too is a holiday")
myfile.close()

myfile = open("output.txt", "a")
myfile.write("My name is Pranav")
myfile.write("working on python")
myfile.write("to enhance my skills")
myfile.write("Saturday is a holiday")
myfile.write("Sunday too is a holiday")
myfile.close()