def decode(encoded_password):
    encoded_list = list(encoded_password)
    for x in range(len(encoded_list)):
        if encoded_list[x] == "0":
            encoded_list[x] = "7"
        elif encoded_list[x] == "1":
            encoded_list[x] = "8"
        elif encoded_list[x] == "2":
            encoded_list = "9"
        else:
            encoded_list[x] = int(encoded_list[x])
            encoded_list[x] = int(encoded_list[x] - 3)
            encoded_list[x] = str(encoded_list[x])
    password = ''.join(encoded_list)
    return password
