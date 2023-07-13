fruits = ["Apple" , "Mango" , "Grapes" , "Banana"] ;
vegitables = ["Broccoli" , "Green peace" , "Tumip"] ;
student_info = ["Naduka" , 24 , "24/1 Gall road, Dehiwala "] ;

# update a data inside the list

fruits[0] = "Green apple" ;
print (fruits) ;
student_info[0] = "Yomal" ;
print (student_info) ;

# add a data into the list

student_info = student_info + ["python"] ;  # This will add to end of the list
student_info = [123] + student_info ; # This will add in front of the list 
print (student_info) ;

# Membership Operator

# We use "in and not in" to check the membership in a list we recieve "true and false" as a out put
print ("Apple" in fruits) ;
print ("Green apple" in fruits) ;

name = "Naduka" in student_info ;

print (name) ;
print ("Naduka"  not in student_info) ;
print ("a" in "Apple") ;
print ("A" in "Apple") ;

# get the length of the list

print (len(student_info)) ;
# print (len(student_info[0])) ; #this will recieve an error, becuse we cant get lenth in a integer data type
print (len(student_info[1])) ;

# get maximum and minimum value

numbers = [1,2,5,8,10,20] ; 

print (max(numbers)) ;
print (min(numbers)) ;

# Convert String to the List

company_name = "ABC pvt" ;
company_name_L = list (company_name) ;

print (company_name_L) ;

# Delete data from the list

del(numbers[0]);
del(numbers[0:3]);
print (numbers) ;