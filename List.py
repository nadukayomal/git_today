fruits = ["Apple" , "Mango" , "Grapes" , "Banana"] ;
vegitables = ["Broccoli" , "Green peace" , "Tumip"] ;
student_info = ["Naduka" , 24 , "24/1 Gall road, Dehiwala "] ;

# We use List to store collection of data under the singale variable most of the language called this type as Array,but in Python it is streange.
# We use "," symble to seperate each date inside the List

print (fruits) ;
print (vegitables) ;
print (student_info) ;

    # Concadinate

print("\t\t Addition") ;

vegi_and_fruits = vegitables + fruits ;
print(type(vegi_and_fruits)) ;
print (vegi_and_fruits) ;

    # Multiplication

print("\t\t Multiplication") ;

print (fruits * 3) ;
print (type(fruits * 3)) ;

    # Slice Operators

print("\t\t Slice Operators") ;
     
print (fruits[0]) ;
print (fruits[0][0]) ;
print (fruits[0][1]) ;
print (fruits[0][2]) ;
print (fruits[0][3]) ;
print (fruits[0][4]) ;
print (fruits[1]) ;
print (fruits[2]) ;
print (fruits[3]) ;

print (student_info[0]) ;
print (student_info[1]) ;
print (student_info[2]) ;
print (student_info[0][0]) ;
# print (student_info[1][0]) ; This command will be a error because we cant give the slice operator to the int data type in side the List 

print (student_info[0] + " like to eat " + fruits[0]) ;