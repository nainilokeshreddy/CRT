'''
#1.pascal triangle
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascal(n):
    triangle = pascal_triangle(n)
    for row in triangle:
        print(' '.join(map(str, row)))

n = int(input("Enter number of rows: "))
print_pascal(n)
'''
'''
#2. butterfly pattern
def butterfly_pattern(n):
    for i in range(1, n + 1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
    for i in range(n, 0, -1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i) 
n = int(input("Enter the size of the butterfly pattern: "))
butterfly_pattern(n)
'''