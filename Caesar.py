import easygui
import os

"""

    Implementing Caesar cipher in different scenarios:
    Shifting right/left operations
    Brute-force all combinations
    Finding the key used to shift

"""
def main():
    print("Welcome to Caesar Shift cipher !!!!!")
    caesar_cipher()


def lowercase_shift(lowercase_input, time):
    value = ord(lowercase_input)
    # if value == 32:
    #    return value
    # if the ascii value is greater tha 122 go start from 97
    if value + time > 122:
        # we have subtracted the value from the last value of ascii
        result = time - (122 - value)
        # then start again
        output = chr(96 + (result % 26))
    else:
        output = chr(value + time)
    return output


def uppercase_shift(uppercase_input, time):
    value = ord(uppercase_input)
    # if the ascii value is greater tha 90 go start from 65
    if value + time > 90:
        # we have subtracted the value from the last value of ascii
        result = time - (90 - value)
        # then add again to start
        output = chr(64 + (result % 26))
    else:
        output = chr(value + time)
    return output


def shift_brute_force(user_input):
    print("Brute-force")
    for i in range(1, 25):
        output = ''
        for j in range(len(user_input)):
            if user_input[j].isupper():
                output += uppercase_shift(user_input[j], i)
            elif user_input[j].islower():
                output += lowercase_shift(user_input[j], i)
            else:
                output += user_input[j]
        print("The string after shifting ", i, "times is :", output)


def find_key():
    user_input = input("Enter the string : ")
    target = input("Enter the decoded string: ")
    for i in range(1, 25):
        output = ''
        for j in range(len(user_input)):
            if user_input[j].isupper():
                output += uppercase_shift(user_input[j], i)
            elif user_input[j].isupper():
                output += lowercase_shift(user_input[j], i)
            else:
                output += user_input[j]
        if output == target:
            print("The key used for shifting is :", i);
            break;


def shift_operation(user_input, shift, shift_time):
    output = ''  # final output
    for i in range(len(user_input)):
        # add/ subtract how many times the shift have to be performed on that string
        if user_input[i].isupper():
            output += uppercase_shift(user_input[i], shift_time)
        elif user_input[i].islower():
            output += lowercase_shift(user_input[i], shift_time)
        else:
            output += user_input[i]
    print("The string after shifting is : " + output)


def caesar_cipher():
    # give options to the user whether they want any particular shift or brute force combinations
    # for now I am only checking for the lower/upper alphabets and space.
    while True:
        print("Options: ")
        print("1. Shift operation for particular key")
        print("2. Brute-force all the combinations")
        print("3. Find out the key")
        print("4. Exit")
        choice = int(input("Please enter the choice : "))

        if choice == 1:
            # take the input from the user
            user_input = input("Enter the string: ")
            #  ask for the which type of shift
            shift = input("Provide what type of shift needs to perform (Right/left) :")
            # ask how many times shift need to be performed
            shift_time = int(input("How many times the string need to be shifted: "))
            if shift.lower() == 'right':
                shift_operation(user_input, shift, shift_time)
            else:
                shift_time = 26- shift_time
                shift_operation(user_input, shift, shift_time)
        elif choice == 2:
            # take the input from the user
            user_input = input("Enter the string: ")
            # all the combinations
            shift_brute_force(user_input)
        elif choice == 3:
            # needed work
                find_key()
        else:
            exit()


if __name__ == "__main__":
    main()