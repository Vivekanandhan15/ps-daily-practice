def remove_spaces(text):
    no_spaces = ""
    for ch in text:
        if ch != " ":
            no_spaces += ch
    print(no_spaces)

remove_spaces(input("Enter a sentence : "))