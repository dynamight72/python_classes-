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
     for a in range(2,q):
        if q%a==0:
            print("It is not a Prime.")
            break
        else:
            print("It is a Prime.")


#Part Four
print("Part Five")
interval = int(input("Interval Please:"))
print("Prime numbers between",interval,"are:")
for num in range(interval + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

#Part Five
num = int(input("Number please:"))
while 1 <= input:
       if input*range(1,input):
              print(input)
       input = input + 1




#part five


