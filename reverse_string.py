
def reverse_string_inbuilt(s):
    print(s[::-1])

# Reverse string without using slicing

def reverse_string(s):
   
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    print(reversed_str)

s = input("Enter a string :") 

reverse_string_inbuilt(s)
reverse_string(s)