

# Using inbuilt split()

def split_on_hyphen(sentence):
    
    words = sentence.split("-")
    for word in words:
        print(word)

# Without using split()

def split_on_hyphen_manual(sentence):

    temp = ""
    for char in sentence:
        if char != "-":
            temp += char
        else:
            print(temp)
            temp = ""
    print(temp) 

sentence = "Emma-is-a-data-scientist"    
split_on_hyphen(sentence)
split_on_hyphen(sentence)
