from sys import argv

# arguments that are given on the command line
script, filename = argv

txt = open(filename) # txt is assigned a file that can take commands

print "Here's your file %r:" % filename
print txt.read() # read is a command (method) used on the file

# Study Drills
script2 = raw_input("Enter script file name... ")
filename2 = raw_input("Enter text file name... ")

txt2 = open(filename2)

print "Here's your file %r:" % filename2
print txt2.read()


