num_1 = int(input("Enter num 1 : "))
num_2 = int(input("Enter num 2 : "))

try:
    div = num_1/num_2
    print(div)
except ZeroDivisionError:
    print("Zero divition error")
else:
    print("No any error")

def modarate(marks):
    updated_marks_list = []
    for i in marks:
        final_result = modarate_value + i
        updated_mark_list.append(final_result)
    return updated_marks_list