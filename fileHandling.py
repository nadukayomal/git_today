# read file

file_object = open("input1.txt","r")

#name = file_object.read()
#print(name)

#name1 = file_object.readline().strip()
#name2 = file_object.readline().strip()
#name3 = file_object.readline().strip()
#name4 = file_object.readline()

#print(name1)
#print(name2)
#print(name3)
#print(name4)

for i in file_object:
    print(i.strip())

file_object.close()

print("\n")

file_object_1 = open(".//readfiles//input2.txt","r")

for line in file_object_1:
    print(line.strip())

file_object_1.close()