def encode(password):
    password_string = str(password) # converts integer password into a string
    pw_digits = [] # empty array to put individual digits of password into
    encoded_password = ""

    for i in range(len(password_string)): # adds digits from password into array
        pw_digits.append(password_string[i])

    for i, digit in enumerate(pw_digits): # converts each element back into a string
        pw_digits[i] = int(digit)

    for digit in pw_digits: # encodes elements and inserts them into string variable
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

def decode(secret):
    ta_da = ''
    for i in secret:
        receiver = int(i)
        receiver -= 3
        if receiver < 0:
            receiver += 10
        ta_da += str(receiver)
    print(f"The encoded password is {secret}, and the original password is {ta_da}")
    print("")


if __name__ == "__main__": # main function
    stop_menu = False
    user_password = 0
    user_encoded_password = ""

    while stop_menu is False: # menu loop
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode \n3. Quit\n")
        choice_user = int(input("Please enter an option: "))

        if choice_user == 1: # encodes user password
            user_password = str(input("Please enter your password to encode: "))
            user_encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")

        elif choice_user == 2:
            decode(user_encoded_password)
        elif choice_user == 3: # breaks loop and ends program
            stop_menu = True
            break
        print()

