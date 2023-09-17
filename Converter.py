from CryptoManagerFactory import CryptoManagerFactory
import base64
import json


def format_content_and_key(content_data, client_public_key):
    # Converte o conteúdo
    content_data = base64.b64decode(content_data)

    # Faz a descriptografia com a chave privada
    crypto_manager_factory = CryptoManagerFactory()
    manager = crypto_manager_factory.get_crypto_manager()
    mensagem = manager.decrypt(content_data)

    # Converte o texto claro em JSON e acessa o conteúdo
    mensagem = json.loads(mensagem)

    # Ajusta a chave
    process_public_key = client_public_key.replace('b\'-----', '-----')
    process_public_key = process_public_key.replace('-----\'', '-----')
    process_public_key = bytes(process_public_key, 'utf-8')
    process_public_key = process_public_key.replace(b'\\n', b'\n')

    # Retorna valores
    return mensagem, process_public_key


def format_return(client_public_key, message_return):
    # Faz a criptografia do retorno
    crypto_manager_factory = CryptoManagerFactory()
    manager = crypto_manager_factory.get_crypto_manager()
    mensagem = manager.encrypt(message_return, client_public_key)
    mensagem = base64.b64encode(mensagem).decode('utf-8')
    return mensagem
