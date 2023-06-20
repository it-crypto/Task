def shift_operation(user_input, shift, shift_time):
    output = ''  # final output
    result = ''  # to convert lower case back after processing.

    if shift.lower() == 'right':
        for i in range(len(user_input)):
            flag_lower = 0
            # add/ subtract how many times the shift have to be performed on that string
            # converting all the lower case letters for conversion after processing I will convert back
            if user_input[i].islower():
                flag = 1
                value = chr(ord(user_input[i]) - 32)
                user_input[i] = value

            # store the shift_time so
            restore_shift = shift_time

            shift_add = ord(user_input[i])  # convert to ascii
            # check if it is space if it is then add space only
            if shift_add == 32:
                output += chr(shift_add)
            else:
                # if the ascii value is greater tha 90 go start from 65
                if shift_add + shift_time > 90:
                    # we have subtracted the value from the last value of ascii
                    shift_time -= (90 - shift_add)
                    # then add again to start
                    result += chr(64 + (shift_time % 26))
                else:
                    result += chr(shift_add + shift_time)

                shift_time = restore_shift
        if flag_lower == 1:
            output += result.lower()
        else:
            output += result

    else:
        output = ''
        for i in range(len(user_input)):
            shift_add = ord(user_input[i])  # convert to ascii
            # check if it is space if it is then add space only
            if shift_add == 32:
                output += chr(shift_add)

            value = ord(user_input[i])
            diff = value - shift_time
            if diff < 65:
                value = 91 - (65 - (shift_time))
                output += chr(value)
            else:
                output += chr(diff)

'''
// for left shift I have tried something but 
    else:
        for i in range(len(user_input)):
            # add/ subtract how many times the shift have to be performed on that string
            # as if it is left shift I am subtracting the value from 26 so that it acts as right shift
            shift_time = 26 - shift_time
            if user_input[i].isupper():
                output += uppercase_shift(user_input[i], shift_time)
            elif user_input[i].islower():
                output += lowercase_shift(user_input[i], shift_time)
            else:
                output += user_input[i]


'''