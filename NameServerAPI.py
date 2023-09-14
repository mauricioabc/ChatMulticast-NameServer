from flask import Flask, request, jsonify
from NameServerManager import NameServerManager
from CryptoManagerFactory import CryptoManagerFactory
import binascii

app = Flask(__name__)


@app.route('/createchat', methods=['POST'])
def process_create_chat():
    try:
        data = request.get_json()  # Obtém o JSON da solicitação

        # Verifica se o JSON contém as chaves necessárias
        chat_name = data.get('chat_nome')
        chat_ip = data.get('chat_ip')
        chat_port = data.get('chat_port')
        chat_password = data.get('chat_password')

        if chat_name is not None and chat_ip is not None and chat_port is not None and chat_password is not None:
            manager = NameServerManager()
            messa_return, status_return = manager.insertNewMulticastChat(chat_name, chat_ip, chat_port, chat_password)
            return jsonify({'status': 'success', 'message': messa_return})
        else:
            return jsonify({'status': 'error',
                            'message': 'O JSON deve conter as chaves "chat_nome", "chat_ip" e "chat_port"}'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/updatechattuple', methods=['POST'])
def process_update_chat_tuple():
    try:
        data = request.get_json()  # Obtém o JSON da solicitação

        # Verifica se o JSON contém as chaves necessárias
        chat_name = data.get('chat_nome')
        chat_ip = data.get('chat_ip')
        chat_port = data.get('chat_port')

        if chat_name is not None and chat_ip is not None and chat_port is not None:
            manager = NameServerManager()
            messa_return, status_return = manager.updateChatIpAndPortByName(chat_name, chat_ip, chat_port)
            return jsonify({'status': 'success', 'message': messa_return})
        else:
            return jsonify({'status': 'error',
                            'message': 'O JSON deve conter as chaves "chat_nome", "chat_ip" e "chat_port"}'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/updatechatkey', methods=['POST'])
def process_update_chat_key():
    try:
        data = request.get_json()  # Obtém o JSON da solicitação

        # Verifica se o JSON contém as chaves necessárias
        chat_name = data.get('chat_nome')
        chat_key = data.get('chat_key')

        if chat_name is not None and chat_key is not None:
            manager = NameServerManager()
            messa_return, status_return = manager.updateChatCryptoKeyByName(chat_name, chat_key)
            return jsonify({'status': 'success', 'message': messa_return})
        else:
            return jsonify({'status': 'error',
                            'message': 'O JSON deve conter as chaves "chat_nome", "chat_ip" e "chat_port"}'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/deletechat', methods=['POST'])
def process_delete_chat():
    try:
        data = request.get_json()  # Obtém o JSON da solicitação

        # Verifica se o JSON contém as chaves necessárias
        chat_name = data.get('chat_nome')

        if chat_name is not None:
            manager = NameServerManager()
            messa_return, status_return = manager.deleteChatByName(chat_name)
            return jsonify({'status': 'success', 'message': messa_return})
        else:
            return jsonify({'status': 'error',
                            'message': 'O JSON deve conter as chaves "chat_nome", "chat_ip" e "chat_port"}'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/getchatkey', methods=['POST'])
def process_get_chat_name():
    try:
        data = request.get_json()  # Obtém o JSON da solicitação

        # Verifica se o JSON contém as chaves necessárias
        chat_name = data.get('chat_nome')

        if chat_name is not None:
            manager = NameServerManager()
            chat_data = manager.getChatByName(chat_name)
            if chat_data:
                return jsonify({'status': 'success', 'chat_data': chat_data})
            else:
                return jsonify({'status': 'error', 'message': f'Chat "{chat_name}" not found'}), 404
        else:
            return jsonify({'status': 'error', 'message': 'O JSON deve conter a chave "chat_nome"'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/connection', methods=['POST'])
def process_test_connection():
    if request.method == 'POST':
        crypto_manager_factory = CryptoManagerFactory()
        manager = crypto_manager_factory.get_crypto_manager()
        server_public_key = manager.server_public_key
        server_public_key = binascii.hexlify(server_public_key).decode('utf-8')
        return jsonify({'server_public_key': server_public_key, 'server_status': 'online'})
    else:
        return jsonify({'erro': 'Esta rota só aceita solicitações POST'}), 400


@app.route('/', methods=['GET'])
def process_server_default_message():
    if request.method == 'GET':
        return jsonify({'server_message': 'Bem-Vindo ao Servidor de Chaves', 'server_status': 'online'})
    else:
        return jsonify({'erro': 'Esta rota só aceita solicitações POST'}), 400
