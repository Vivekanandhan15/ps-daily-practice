sentence = "Emma-is-a-data-scientist"

# Using inbuilt split()

words = sentence.split("-")
for word in words:
    print(word)

# Without using split()

sentence = "Emma-is-a-data-scientist"

temp = ""
for char in sentence:
    if char != "-":
        temp += char
    else:
        print(temp)
        temp = ""
print(temp)