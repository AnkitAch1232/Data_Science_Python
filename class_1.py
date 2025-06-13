#data structures
#List
my_list1 = [1,1,3,4]
my_list2 = ["ankit","ankit","sunil"]
#Tuple
my_tuple = (1,1,3,4)
my_tuple2 = ("ankit","ankit","sunil")
#Set
my_set = {1,1,3,4}
my_set2 = {"ankit","ankit","sunil"}
#Dictinory
my_dictinory1 = {"a":22,"b":23,"c":24}
my_dictinory2 = {"ankit":1, "ankit":2,"sunil":3}

#Print
print(my_list1)
print(my_list2)
print(my_tuple)
print(my_tuple2)
print(my_set)
print(my_set2)
print(my_dictinory1)
print(my_dictinory2)

#print specific data
print(my_list2[1])
print(my_tuple2[1])
print(my_set2)
print(my_dictinory2['ankit'])


#changing dictinory data
my_dictinory2['ankit'] = 22
print(my_dictinory2['ankit'])

#for loop to print set
for i in my_set:
    print(i);

#adding new value
my_list1.append(6)
my_set.add(5)  
my_dictinory1['d']=4 
print(my_list1)
print(my_set)
print(my_dictinory1)
