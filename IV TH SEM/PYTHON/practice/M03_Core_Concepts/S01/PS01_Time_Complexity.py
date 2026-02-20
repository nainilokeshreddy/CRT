def Linear_Search(elements, target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1
print(Linear_Search([1, 2, 3, 4, 5], 3))  # Output: 2