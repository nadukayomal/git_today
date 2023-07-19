# file possition
file_object = open(".//readfiles//output1.txt","a")

# check possition
possition = file_object.tell()
print("File location is ",possition)

# change possition
possition_2 = file_object.seek(0,1)
print("File location is ",possition_2)

file_object.close()