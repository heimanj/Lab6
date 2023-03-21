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

def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    menu_option = int(input("Please enter an option: "))
    if menu_option == 1:
        encode_password = input("Please enter your password to encode: ")
        encode(encode_password)
        print("Your password has been encoded and stored!")
    elif menu_option == 2:
        pass
    elif menu_option == 3:
        quit()

if __name__ == "__main__":
    main()

