first_name = "Naduka";
middle_name = "Yomal";
last_name = "Nayanodya";

# Operators for string

    # + add/concadinate
full_name = first_name + middle_name + last_name;
print(full_name);

fullName = first_name + " " + middle_name + " " + last_name;
print(fullName);

_space = " ";
_full_name = first_name + _space + middle_name + _space + last_name;
print(_full_name);

    # * multiplication
print(first_name * 2);
print((first_name + _space )* 2);
print(fullName * 3);

    # slice operators (use for get data from seperately in a string)

print(first_name);
print(first_name[0:2]);
print(first_name[1::2]);

slice_full_name = full_name[:6];
slice_full_name_1 = full_name[:6:1];

print (slice_full_name); 
print (slice_full_name_1); 

print(first_name[0]);
print(first_name[1]);
print(first_name[2]);
print(first_name[3]);
print(first_name[4]);
print(first_name[5]);

print(first_name[-6:-1]);
print(first_name[-1:-7:-1]);
print(first_name[-1:-8:-1]);

# print (first_name[7]) ;

print(first_name);

#Escape charactors

    # \a = alert.bell
    # \n = new line
    # \t = tab
    # \" = double quatation
    # \' = singal quatation

print("Naduka\nYomal \" CEO \"");
print("Naduka\tYomal \" CEO \"");
print("\' Naduka Yomal \'");
print("Naduka \a Yomal");



print(first_name[0]);
print(first_name[1]);
print(first_name[2]);
print(first_name[3]);
