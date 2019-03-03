# #Part one
# num_tuple = ("verro","Hello","23",55,23,78,True,False,True,1.34,2.34,6.84)
#
# #part two
# for num in num_tuple:
#     print(type(num))
#     print(type(num)==int)
#
# #Part 3
# print(num_tuple[0:3])
# print(num_tuple[3:6])
# print(num_tuple[6:9])
# print(num_tuple[9:12])

#part 4
dictionary = {"sid":"Siddhanth","dha":"is"}
print(dictionary)
dictionary["nth"] = "cool"
print(dictionary)

#part 5
import random
print("Your random number is: ",random.randint(1,13))
randomnum = random.randint(1,13)
def primenum(s):
    g = s
    if g > 1:
       for i in range(2,g):
           if (s % i) == 0:
               print("False")
               break
           else:
               print("True")
t = random.randint(1,13)
print(primenum(t))


# #part 6
# import json
# y = json.loads('{"error":{"code":400,"message":"Bad Request"}}')
# type(y)
# x = dict(y)
# print(x['error'])
#
# #part 7
# listy = [1,2,3,4,5,6,7,8,9,0]
# for l in listy:
#     print()

