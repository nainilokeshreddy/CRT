'''1. Square Star Pattern
n = 4
output:
* * * *
* * * *
* * * *
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''
'''2.Right angle triangle
n = 4
*
* * 
* * *
* * * *

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()
'''
'''3.Inverted Triangle
n = 4
* * * *
* * *
* *
*

n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end = " ")
    print()
'''
'''4.Number Triangle
n = 4
Output:
1
1 2
1 2 3
1 2 3 4

n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end = " ")
    print()
'''
'''5.Reapeted number pattern
n = 4
output:
1
2 2
3 3 3
4 4 4 4

n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
'''
'''6. Alphabet triangle
n = 4
Output:
A
A B
A B C
A B C D
'''
'''
8.Hollow sphere
n =4
* * * *
*     *
*     *
* * * *
'''