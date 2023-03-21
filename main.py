# Jason Heiman
def encode(password):
    password_list = list(password)
    for x in range(len(password_list)):
       if password_list[x] == "7":
           password_list[x] = "0"
       elif password_list[x] == "8":
           password_list[x] = "1"
       elif password[x] == "9":
           password_list[x] = "2"
       else:
           password_list[x] = int(password_list[x])
           password_list[x] = password_list[x] + 3
           password_list[x] = str(password_list[x])
    encoded_password = ''.join(password_list)
    return encoded_password


# Michael Neff-Flahan
def to_unencoded(password):
    password_final = []
    password = str(password)
    for x in range(len(password)):
        password_final = password_final + [unencode_one(password[x])]
    password_final = ''.join(password_final)
    return password_final

def unencode_one(x):
    x = int(x)
    if x in [3, 4, 5, 6,7, 8, 9]:
        x -= 3
    elif x in [0, 1, 2]:
        x += 7
    return str(x)


def main():
    encode_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            encode_password = str(input("Please enter your password to encode: "))
            encode_password = encode(encode_password)
            print("Your password has been encoded and stored!")
        elif menu_option == 2:
            decoded_password = to_unencoded(encode_password)
            print("The encoded password is", encode_password, "and the original password is", decoded_password)

        elif menu_option == 3:
            quit()

if __name__ == "__main__":
    main()

