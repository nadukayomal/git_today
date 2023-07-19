def my_function():
   a = 5
   b = 10
   c = a + b
   return c
    
#total = my_function()
#print(total)

def calculate_squere(number):
    return number**2
    
squere = calculate_squere(5)
print(squere)

# Key word argument

def stu_info(name,age):
    print("Name : ",name)
    print("Age : ",age)
   
stu_info("Naduka",23)

# default argument

def emp_info(name,age = 23):
    print("Name : ",name)
    print("age : ",age)
    
emp_info("Yomal")

def moderate(marks_list, moderate_value = 5):
    updated_marks_list = []
    for i in marks_list:
        final_result = i + moderate_value
        updated_marks_list.append(final_result)
    return updated_marks_list

marks = [30, 35, 40, 20, 10, 80, 70 , 75, 55, 85]
marks = sorted(marks)
pass_mark = 40
moderateValue = pass_mark - marks[2]

moderated_marks = moderate(marks, moderateValue) 

print(marks)
print(moderated_marks)