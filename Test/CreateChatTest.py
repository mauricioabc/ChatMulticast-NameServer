import unittest
from NameServerManager import NameServerManager


class MyTestCase(unittest.TestCase):
    def test_create_new_chat(self):
        manager = NameServerManager()
        manager.insertNewMulticastChat('Teste', '192.168.1.1', 8000)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
