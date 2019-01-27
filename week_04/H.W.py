# #part 1
# print("Part One")
# n = int(input("number please"))
# print(n%2)
# if n%2<1 :
#             print("It is divisible by 2.")
# if n%2>0 :
#         print("It is not divisible.")
#
# #part 02
# print("Part Two")
# n = int(input("number please"))
# print(n%6)
# if n%6<1 :
#             print("It is divisible by 6.")
# if n%6>0 :
#         print("It is not divisible.")
#
# #part 3
# print("Part Three")
# ab = str(input("Number please"))
# d = int(input("Number please"))
# if ab[0]<d :
#     print("Ok.......")
#     if ab[1]<d :
#      print("It contains ",d)
# else:
#     print("It doesnt contain ",d)
#
# #part 04
# print("Part Four")
# a = int(input("Please give the number."))
# b = int(input("Please give the number."))
# ab = a+b
# print(ab)
# if ab>a**b :
#     print("Yes it is greater.")
# print(a**b)
# if ab<a**b :
#     print("No it is not greater.")
#     print(a**b)

#part 05
print("Part Five")
a = int(input("Please give the number."))
b = int(input("Please give the number."))
x = int(input("Please give the number."))
apowerb = a**b
print(apowerb)
xm1 = apowerb+x/2
xm2 = xm1-(xm1%x)
print(xm2)
