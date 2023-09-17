import requests
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from CryptoManager import CryptoManager

manager = CryptoManager()
priv, pub = manager.generate_server_asym_keys('teste123')

# URL para obter a chave pública do servidor
server_public_key_url = "http://127.0.0.1:5000/connection"

# URL para enviar o texto criptografado e a chave pública do cliente
send_chat_key_url = "http://127.0.0.1:5000/getchatkey"

# Realize a solicitação HTTP para obter a chave pública do servidor
response = requests.post(server_public_key_url)

if response.status_code == 200:
    # Parse a chave pública do servidor do JSON de resposta
    server_public_key_data = json.loads(response.text)
    process_public_key = server_public_key_data["server_public_key"]
    process_public_key = process_public_key.replace('b\'-----', '-----')
    process_public_key = process_public_key.replace('-----\'', '-----')
    process_public_key = bytes(process_public_key, 'utf-8')
    process_public_key = process_public_key.replace(b'\\n', b'\n')
    server_public_key = RSA.import_key(process_public_key)

    # Texto a ser criptografado
    plaintext = {
        "chat_nome": "TesteServer"
    }
    plaintext_json = json.dumps(plaintext)

    # Criptografe o texto com a chave pública do servidor
    cipher = PKCS1_OAEP.new(server_public_key)
    ciphertext = cipher.encrypt(plaintext_json.encode('utf-8'))

    # Construa o JSON a ser enviado
    encrypted_data = {
        "data": base64.b64encode(ciphertext).decode('utf-8'),
        "client_public_key": str(pub)
    }

    # Realize a solicitação HTTP para enviar o texto criptografado e a chave pública do cliente
    response = requests.post(send_chat_key_url, json=encrypted_data)
    print(response.text)
    retorno = response.text
    retorno = json.loads(retorno)
    retorno = retorno.get('chat_data')
    retorno = base64.b64decode(retorno)

    priv = RSA.import_key(priv, passphrase='teste123')
    cipher = PKCS1_OAEP.new(priv)
    decrypted_message = cipher.decrypt(retorno).decode('utf-8')
    # decrypted_message = json.loads(decrypted_message)
    print(decrypted_message)

    if response.status_code == 200:
        print("Mensagem criptografada e chave pública do cliente enviadas com sucesso.")
    else:
        print("Falha ao enviar mensagem criptografada e chave pública do cliente.")
else:
    print("Falha ao obter a chave pública do servidor.")
