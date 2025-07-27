def encrypt():
    msg = input("message: ")
    key = input("key: ")
    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        deciText = ord(msg[i]) ^ ord(key[key_itr])
        key_itr+=1

        if key_itr >= len(key):
            key_itr = 0


        encrypt_hex += hex(deciText)[2:]

    print(f"message encrypted successfully!\nmessage: {encrypt_hex}")
    s = input(": ")


def decrypt():
    msg = input("message: ")
    key = input("key: ")
    hex2uni = ""
    key_itr = 0
    decrypt_text = ""
    for i in range(0,len(msg),2):
        hex2uni+=bytes.fromhex(msg[i:i+2]).decode('utf-8')
        

    for i in range(len(hex2uni)):
        temp = ord(hex2uni[i]) ^ ord(key[key_itr])
        decrypt_text += chr(temp)

        key_itr+=1
        if key_itr >= len(key):
            key_itr = 0

    print(f"the decrypted message is: {decrypt_text}")
    q = input(": ")

print("================================")
print("====== nati encrypter ==========")
print("================================")




user = input("what did you want to do\n1.encrypt\n2.decrypt\n: ")
if user == '1':
    encrypt()
elif user == '2':
    decrypt()
else:
    print("invalid entery you can only enter 1 and 2")


    