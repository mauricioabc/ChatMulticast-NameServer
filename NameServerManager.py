from datetime import datetime
from DatabaseManager import session_factory
from ChatMulticastInfo import ChatMulticastInfo
from CryptoManager import CryptoManager
import binascii


class NameServerManager:
    def __init__(self):
        self.connection = None
        self.session = session_factory()
        self.crypto_manager = CryptoManager()

    # Insere novo registro de chat
    def insertNewMulticastChat(self, chat_name, ip_addr, port, password):
        # Verifica se o chat já existe no banco de dados
        existing_chat = self.session.query(ChatMulticastInfo).filter_by(Name=chat_name).first()
        if existing_chat is None:
            newMulticastChat = ChatMulticastInfo(Name=chat_name, IpAddress=ip_addr,
                                                 Port=port, InsertDate=datetime.now())
            self.session.add(newMulticastChat)
            self.session.commit()
            self.updateChatCryptoKeyByName(chat_name, password)
            return "New multicast chat inserted successfully.", "success"
        else:
            return "Multicast chat already exists: Insertion blocked.", "failure"

    # Atualiza o ip e a porta de um chat pelo nome
    def updateChatIpAndPortByName(self, chat_name, new_ip_addr, new_port):
        existing_chat = self.session.query(ChatMulticastInfo).filter_by(Name=chat_name).first()
        if existing_chat:
            existing_chat.IpAddress = new_ip_addr
            existing_chat.Port = new_port
            self.session.commit()
            return f"Chat '{chat_name}' updated successfully.", "success"
        else:
            return f"Chat '{chat_name}' not found. Update operation failed.", "failure"

    # Atualiza a chave simétrica de um chat pelo nome
    def updateChatCryptoKeyByName(self, chat_name, password):
        existing_chat = self.session.query(ChatMulticastInfo).filter_by(Name=chat_name).first()
        if existing_chat:
            new_chat_crypto_key = self.crypto_manager.generate_sym_key(password)
            new_chat_crypto_key = binascii.hexlify(new_chat_crypto_key).decode('utf-8')
            existing_chat.ChatCryptoKey = new_chat_crypto_key
            self.session.commit()
            return f"Chat '{chat_name}' updated successfully.", "success"
        else:
            return f"Chat '{chat_name}' not found. Update operation failed.", "failure"

    # Remove um chat pelo nome
    def deleteChatByName(self, chat_name):
        existing_chat = self.session.query(ChatMulticastInfo).filter_by(Name=chat_name).first()
        if existing_chat:
            self.session.delete(existing_chat)
            self.session.commit()
            return f"Chat '{chat_name}' deleted successfully.", "success"
        else:
            return f"Chat '{chat_name}' not found. Deletion operation failed.", "failure"

    # Retorna a chave de um chat
    def getChatByName(self, chat_name):
        existing_chat = self.session.query(ChatMulticastInfo).filter_by(Name=chat_name).first()
        if existing_chat:
            chat_data = {
                'Name': existing_chat.Name,
                'IpAddress': existing_chat.IpAddress,
                'Port': existing_chat.Port,
                'ChatCryptoKey': existing_chat.ChatCryptoKey,
                'InsertDate': existing_chat.InsertDate.strftime('%Y-%m-%d %H:%M:%S')
            }
            return chat_data
        else:
            return None
