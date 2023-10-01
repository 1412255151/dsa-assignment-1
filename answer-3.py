def are_strings_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated_str = str1 + str1
    if str2 in concatenated_str:
        return True
    else:
        return False


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


if are_strings_rotations(str1, str2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
