def encode(password):
    password_string = str(password) # integer password to a string
    pw_digits = [] # empty array
    encoded_password = ""

    for i in range(len(password_string)): # password into array
        pw_digits.append(password_string[i])

    for i, digit in enumerate(pw_digits): # converts each element back into a string
        pw_digits[i] = int(digit)

    for digit in pw_digits: # inserts elements into string variable
        if digit in range(0, 7):
            digit += 3
            encoded_password += str(digit)
        elif digit == 7:
            encoded_password += "0"
        elif digit == 8:
            encoded_password += "1"
        elif digit == 9:
            encoded_password += "2"
        elif digit == 0:
            encoded_password += "3"

    return encoded_password

