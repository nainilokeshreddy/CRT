#1. find largest number (Using max() function)
'''
numbers = [10, 20, 5, 15]
print(max(numbers))  # Output: 20
'''
#2. check palindrome (USing reversed() % join())
'''
word = input()
if word == ''.join(reversed(word)):
    print("Palindrome")
else:
    print("Not a palindrome")
'''
#3. count even numbers (USing filter())
'''
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
'''
#7. Find  common elements (using set())
'''
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements)  # Output: [4, 5]
'''