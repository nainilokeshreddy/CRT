"""
# to print a word as many times
i = 0
while i < 5:
    print("Hello World")
    i += 1
"""
"""
# to find out no of digits
n = int(input())
i = 0
while n > 0:
    digit = n % 10
    i += 1
    n = n // 10
print(i)
"""
'''
#input:[1,2,3,4,5] output:[1,4,9,16,25]
li = [1,2,3,4,5]
for i in range(len(li)):
    li[i] = li[i] ** 2
print(li)
'''
'''
li = [1,2,3,4,5]
for i in range(len(li)):
    if li[i] % 2 == 0:
        print(li[i], end=" ")
    
li = [1,2,3,4,5]
for x in li:
    if x % 2 == 0:
        print(x,end=" ")
'''
'''
#finding out no of vowels in an string
n = input()
count = 0
for ch in n:
    if ch in "aeiouAEIOU":  
        count += 1
print(count)
'''
