53. Open the file is read & write mode and apply following  functions
         a) All 13 functions mentioned in Tutorial File object table.
Ans:
print "Enter file name to perform operations"
fname=raw_input()
f=open(fname,'rb+')
print "***Name of file-->",f.name
print "***File descriptor no.-->",f.fileno()
print "***is file associated with terminal-->>",f.isatty()
print "***Next line1 print-->",f.next()
print "***Next line2 print-->",f.next()
f.flush()
f.close()
#
f=f=open(fname,'rb+')
print "***read entire file:"
print f.read()
f.close()
#
f=f=open(fname,'rb+')
print "***read first five chars frm file:"
print f.read(5)
f.close()
#
f=f=open(fname,'rb+')
print "***readline***->:"
print "Output of f.readline()-->",f.readline()
print "Output of f.readlines()-->",f.readlines()
f.close()
#
f=f=open(fname,'rb+')
f.seek(0,2)
str="Hello"
f.write( str )
f.seek(0,2)
seq=["line new1","line new2"]
f.writelines(seq)
f.close()
#
f=f=open(fname,'rb+')
print("Output after adding new line-->")
print f.read()
f.truncate()
print "Output after truncate-->",f.readline()
f.close()