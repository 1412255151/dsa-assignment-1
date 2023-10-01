def first_non_repeated_character(s):
    char_count = {}


    for char in s:
        char_count[char] = char_count.get(char, 0) + 1


    for char in s:
        if char_count[char] == 1:
            return char

    return None


input_string = input("Enter a string: ")


non_repeated_char = first_non_repeated_character(input_string)


if non_repeated_char:
    print("The first non-repeated character is:", non_repeated_char)
else:
    print("There are no non-repeated characters in the string.")
