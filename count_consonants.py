text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Number of consonants:", count)