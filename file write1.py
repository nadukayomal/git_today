# write file

file_object_1 = open(".//readfiles//output1.txt","w")

file_object_1.write("Name : Ameer Khan \n")
file_object_1.write("Age : 55 \n")
file_object_1.write("City :Mumbai \n")
file_object_1.write("Education :Indian Institute of Technology")

file_object_1.close()


# read file

file_object_2 = open(".//readfiles//output1.txt","r")

for line in file_object_2:
    print(line.strip())
    
file_object_2.close()
