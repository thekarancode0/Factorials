#write a program to find the factorial of a number

def factorial(num):
    if(num==0 or num==1):
        return 1
    return num*factorial(num-1)


num=int(input("Enter num to find Factorial: "))
result=factorial(num)
print(result)