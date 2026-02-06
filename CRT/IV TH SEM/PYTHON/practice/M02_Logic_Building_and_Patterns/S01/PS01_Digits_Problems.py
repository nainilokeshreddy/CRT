'''
1.count the number of digits in a number
2.find the sum of digits of a number.
3.reverse a number
4.check palindrome number.
5.check armstrong number
6.count even and odd digits.
7.find largest digit.
8.find smallest digit.
9.count zero digits.
10.find digital root of a number.
11.check spy number.
'''
'''
#2.find sum of the digits of a number.
n = int(input())
s = 0
while (n>0):
    s += (n%10)
    n //= 10
print(s)
'''
#10.find digital root of a number.
n = int(input())
while n >10:
    n = sum(list(map(int,str(n))))
print(n)