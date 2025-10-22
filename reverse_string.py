str1 = "Python"
print(str1[::-1])

# Without slicing or inbuilt reverse functions

str1 = "Python"
reversed_str = ""
for ch in str1:
    reversed_str = ch + reversed_str
print(reversed_str)

