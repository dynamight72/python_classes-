num = int(input("Please enter number:"))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print("It is not a prime.")

            break
    else:
        print("It is not a prime.")

#To get odd no in interval
#part six
num2 = int(input("Number please:"))
count = 0
while count <= num2:
       count = count + 1
       if num2 % count == 1:
        break
       else:
        print(count)
        count = count+1

