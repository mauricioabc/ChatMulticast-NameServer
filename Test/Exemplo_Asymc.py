from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def main():
    while True:
        print("1 - Create a new pub/priv key")
        print("2 - Encrypt")
        print("3 - Decrypt")
        selected = int(input("Type de selected option: "))
        if (selected == 1):
            password = input("Type a password: ")
            key = RSA.generate(2048)
            private_key = key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
            private_file = open("private.pem", "wb")
            private_file.write(private_key)
            private_file.close()
            public_key = key.public_key().export_key()
            public_file = open("public.pem", "wb")
            public_file.write(public_key)
            public_file.close()
            break
        elif (selected == 2):
            dest_pub_file_name = input("Type the destination public file name: ")
            dest_pub_file = open(dest_pub_file_name, "rb")
            dest_pub_file_content = dest_pub_file.read()
            dest_pub_key = RSA.importKey(dest_pub_file_content)
            dest_cipher = PKCS1_OAEP.new(dest_pub_key)
            input_file_name = input("Type the input file name: ")
            input_file = open(input_file_name, "rb")
            input_file_content = input_file.read()
            output_file_content = dest_cipher.encrypt(input_file_content)
            output_file = open(input_file_name+".bin", "wb")
            output_file.write(output_file_content)
            output_file.close()
            break
        elif (selected == 3):
            password = input("Type the private key password: ")
            priv_key_file = open("private.pem", "rb")
            priv_key_file_content = priv_key_file.read()
            priv_key = RSA.importKey(priv_key_file_content, passphrase=password)
            cipher = PKCS1_OAEP.new(priv_key)
            input_file_name = input("Type the input file name: ")
            input_file = open(input_file_name, "rb")
            input_file_content = input_file.read()
            output_file_content = cipher.decrypt(input_file_content)
            output_file = open(input_file_name[0:-4], "wb")
            output_file.write(output_file_content)
            output_file.close()
            break


if __name__ == "__main__":
    main()