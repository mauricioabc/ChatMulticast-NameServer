import unittest
from CryptoManagerFactory import CryptoManagerFactory
import requests
import json
import base64


class MyTestCase(unittest.TestCase):
    def test_key_sym(self):
        crypto_manager_factory = CryptoManagerFactory()
        manager = crypto_manager_factory.get_crypto_manager()
        teste = manager.generate_sym_key('P@ssw0rd')
        print(teste)
        self.assertEqual(True, True)  # add assertion here

    def test_key_pair(self):
        crypto_manager_factory = CryptoManagerFactory()
        manager = crypto_manager_factory.get_crypto_manager()
        priv, pub = manager.generate_server_asym_keys('P@ssw0rd')
        print(priv)
        print(pub)
        message = 'Teste de mensagem com acentuação e caractérês especi@is'
        message_crypt = manager.encrypt(pub, message)
        print(message_crypt)
        message_decrypt = manager.decrypt(priv, message_crypt)
        print(message_decrypt)
        self.assertEqual(True, True)  # add assertion here

    def test_keys(self):
        crypto_manager_factory = CryptoManagerFactory()
        manager = crypto_manager_factory.get_crypto_manager()
        teste = manager.server_public_key
        print(teste)

    def test_cript_client(self):
        crypto_manager_factory = CryptoManagerFactory()
        manager = crypto_manager_factory.get_crypto_manager()
        priv, pub = manager.generate_server_asym_keys('P@ssw0rd')
        print(priv)
        print(pub)
        key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr7YOYE4JZcN7G6CZF1oI\nSR2lvnDw0UtMcbSCvxWb5Sg0PTdQNDa3sv7HlfTOkOR7zJXxAyJJZ2GsWvqIYBEj\nMkt/noxdAZQiKT3gpIbUROe1mbqcrpnMmysHBpR+pW2E5XpVVrBa6xwoMt+qq7bx\n9us41HhrFTGkbEGvQOpxo4Y9Rcx8tDwd/Xo9Ye8jDEcMpclkU5ghkHeq98VlO/nW\nO4z7z/PrEg7H3zXG1f+x/shhgLtAJeD4O2w1pfN7fAPAthkhTMuQOuaisHRy3nUS\n/mr0gV6WLlGrH/P5+CmR2eO2n1qaNE9wFTv5/qxm3C6jyHfK5yaiKV2oJiHQqoXk\nkQIDAQAB\n-----END PUBLIC KEY-----'

        message = '{ "chat_nome": "TesteServer" }'
        message_crypt = manager.encrypt(key, message)
        message_crypt = base64.b64encode(message_crypt).decode('utf-8')
        pub = base64.b64encode(pub).decode('utf-8')
        print(message_crypt)

        content_data = base64.b64decode(message_crypt)
        client_public_key = base64.b64decode(pub)

        # message_crypt = base64.b64decode(message_crypt)
        # pub = base64.b64decode(pub)

        # URL da API para a qual você deseja enviar o JSON
        api_url = 'http://127.0.0.1:5000/getchatkey'

        # Dados que você deseja enviar em formato JSON
        data = {
            "data": message_crypt,
            "client_public_key": pub
        }

        # Converte os dados em formato JSON
        json_data = json.dumps(data)

        # Define os cabeçalhos, especificando o tipo de conteúdo como JSON
        headers = {'Content-Type': 'application/json'}

        # Envia a solicitação POST com os dados JSON
        response = requests.post(api_url, data=json_data, headers=headers)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            print('Solicitação bem-sucedida!')
        else:
            print('Erro na solicitação:', response.status_code)
            print('Resposta:', response.text)


if __name__ == '__main__':
    unittest.main()
