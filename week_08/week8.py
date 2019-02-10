# num_list = [1,23,443,5.6]
# num_list[0] = 11111111110000000
# print(num_list)
# # num_tup = (1,23,443,5.6)
# # num_tup[0] = 11111111110000000
# # print(num_tup)
#
# y = (4)
# print(type(y))
# y = (4,)
# print(type(y))
# y = [4]
# print(type(y))

# #dictionary
# dict_employee={"Name":"Siddhanth","Class":"7th","Designation":"Inventor"}
# print(dict_employee["Name"])
# print(dict_employee["Class"])
# print(dict_employee["Designation"])
# dict_employee["Name"]= "Siddhanth Yellanki"
# dict_employee["Class"]= "8th"
# dict_employee["Designation"]= "Senior Inventor"
# # dict_employee.clear()
# # del dict_employee["Age"]
# # print(dict_employee.values())
# # print(dict_employee.keys())
# # print(len(dict_employee))
# print(dict_employee)



# dict_classmate={"Name":"Siddhanth","Class":"7th","Designation":"Inventor"}
# print(dict_classmate["Name"])
# print(dict_classmate["Class"])
# print(dict_classmate["Designation"])
# dict_classmate["Name"]= "Siddhanth Yellanki"
# dict_classmate["Class"]= "8th"
# dict_classmate["Designation"]= "Senior Inventor"
# # dict_classmate.clear()
# # del dict_classmate["Age"]
# # print(dict_classmate.values())
# # print(dict_classmate.keys())
# # print(len(dict_classmate))
# print(dict_classmate)

#random num generation
import random
print(random.randint(1,10))

#json
import json
x='{"Name":"Siddhanth","Class":"7th","Designation":"Inventor"}'
type(x)
y = json.loads(x)
type(y)
print(y["Class"])





