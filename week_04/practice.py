
print("Part Five")
a = int(input("Please give the number."))
b = int(input("Please give the number."))
x = int(input("Please give the number."))
bpowerb = b**b
print(bpowerb)
xm1 = bpowerb+x/2
xm2 = xm1-(xm1%x)
print(xm2)
