'''
1) write a python code for factorial of a number?
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is", factorial) 
'''
'''
2)writee a python code to check whether a number is armstrong or not?
n = int(input("Enter a number: "))
order = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
'''
'''
3)write a python code to check whether a number is prime or not?
n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not a prime number")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")   
'''
'''
4)print the prime number with a range?
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))   
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):        
            if num % i == 0:
                break
        else:
            print(num)
'''
'''
5)Monotonic of an array?

arr = list(map(int, input().split()))
inc = true
dec = true
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        inc = false
    if arr[i] < arr[i + 1]:
        dec = false
if inc or dec:
    print("The array is monotonic")
else:
    print("The array is not monotonic") 
'''
'''
6)reverse a number?
'''
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print("The reverse of the number is:", rev)

