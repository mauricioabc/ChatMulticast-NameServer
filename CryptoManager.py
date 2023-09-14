from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class CryptoManager:
    def __init__(self):
        self.server_private_key, self.server_public_key = self.generate_server_asym_keys('P@ssw0rd')

    def generate_sym_key(self, password):
        salt = b'\x18\x89\xd9i\xf36\xb3\x0e\xa8&.\xf8\xca\x11\x89h\x95w\xe5\xf9\xadV\xa2O\xb8\x8cv\x05\xa8\xef,\xfe'
        key = PBKDF2(password, salt, dkLen=32)
        return key

    def generate_server_asym_keys(self, password):
        key = RSA.generate(2048)
        private_key = key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
        public_key = key.public_key().export_key()
        return private_key, public_key

    def encrypt(self, key, message):
        key = RSA.import_key(key)
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode('utf-8'))
        return encrypted_message

    def decrypt(self, key, password, message):
        key = RSA.import_key(key, passphrase=password)
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(message).decode('utf-8')
        return decrypted_message
