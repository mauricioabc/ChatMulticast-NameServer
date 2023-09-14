from CryptoManager import CryptoManager


class CryptoManagerFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CryptoManagerFactory, cls).__new__(cls)
            cls._instance.initialize_crypto_manager()
        return cls._instance

    def initialize_crypto_manager(self):
        self.crypto_manager = CryptoManager()

    def get_crypto_manager(self):
        return self.crypto_manager