#Part One
p = int(input("Please Give a Number."))
if p>0:
    print("It is a Positive Number.")
if p<0:
    print("It is a Negative Number.")
if p==0:
    print("It is nor Negative neither Positive Number.")

#Part Two
n = int(input("Please Give a Number."))
if (n%2)==0 :
    print("It is an even number.")
else:
    print("It is an Odd Number")

#Part Three
q = int(input("Please give number:"))
if q>1 :
    print("It is a.................")
    if q==2 :
        print("Yes It is a Prime.")
    if (q%2) != 0:
        print("It is an Odd number.")
        if q/2==0:
            print("It is a not Prime.")
        if q/3==0:
            print("It is a not Prime.")
