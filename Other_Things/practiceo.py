# import fibo
# print(fibo.a)

def fibonacci(s):
    count = s
    a = 0
    b = 1
    c = 0
    while c <= count:
        c = a + b
        a = b
        b = c
        print(a)



print(fibonacci(10))

