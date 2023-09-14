import unittest
from CryptoManagerFactory import CryptoManagerFactory

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
        message_decrypt = manager.decrypt(priv, 'P@ssw0rd', message_crypt)
        print(message_decrypt)
        self.assertEqual(True, True)  # add assertion here

    def test_keys(self):
        crypto_manager_factory = CryptoManagerFactory()
        manager = crypto_manager_factory.get_crypto_manager()
        teste = manager.server_public_key
        print(teste)

if __name__ == '__main__':
    unittest.main()
