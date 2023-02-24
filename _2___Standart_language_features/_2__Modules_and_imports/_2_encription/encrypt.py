from simplecrypt import encrypt, decrypt, DecryptionException


data = None
with open("encrypted.bin", "rb") as file:
    data = file.read()

with open("passwords.txt", "r") as file:
    passwords = file.readlines()
    passwords = map(str.strip, passwords)

result = None
for password in passwords:
    try:
        result = decrypt(password, data)
    except DecryptionException:
        print(f"Password '{password}' is incorrect.")
    else:
        print(f"Password '{password}' is correct !\nInfo: {result}")
        break
