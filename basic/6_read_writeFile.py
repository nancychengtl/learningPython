import os
file = open("textFile.txt")
print file.read()
file.close()
file = open("textFile.txt")
print file.readlines()
file.close()
file = open("textFile.txt")
print file.readline()
file.close()

file = open("write.txt", 'w')
 #truncate -- Empties the file. Watch out if you care about the file.
file.truncate()
print("please enter three lines into the file:")
line1 = raw_input("line 1 :")
line2 = raw_input("line 2 :")
line3 = raw_input("line 3 :")
file.write(line1+"\n")
file.write(line2+"\n")
file.write(line3+"\n")
file.close()

# reading files in directory

for file in os.listdir("../training_articles"):
    print str(file)
