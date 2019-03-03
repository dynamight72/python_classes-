#fibonacci sequence
count = int(input("Interval please: "))
a = 0
b = 1
c = 0
while c <= count:
    c = a+b
    a = b
    b = c
    print(a)

