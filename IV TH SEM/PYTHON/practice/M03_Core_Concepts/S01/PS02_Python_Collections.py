# Running sum in id array
nums = [1, 2, 3, 4]
res = []
s = 0
for ele in nums:
    s += ele
    res.append(s)
print(res)  # Output: [1, 3, 6, 10]