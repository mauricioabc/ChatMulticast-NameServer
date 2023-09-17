# API NameServer

Esta é uma API simples para cadastrar e gerenciar informações de Chats Multicasts.

## Instalação

Para começar a usar a API, siga estas etapas:

1. Baixar a última versão do repositório;
2. Instale as dependências:
```bash
py -m pip install -r requirements.txt
ou
pip install -r requirements.txt
```
3. Inicie o servidor:
```bash
python application.py
```
A API estará disponível em `http://localhost:5000`.

## Uso Básico

### Cadastrar um Chat

- **URL:** `/createchat`
- **Método:** POST
- **Corpo da Solicitação:**

```json
{
    "chat_nome": "Teste",
    "chat_ip": "192.168.1.1",
    "chat_port": "8000",
    "chat_password": "teste123"
}
```

### Remover um Chat

- **URL:** `/deletechat`
- **Método:** POST
- **Corpo da Solicitação:**

```json
{
    "chat_nome": "Teste2"
}
```

### Alterar IP e/ou Porta de um Chat

- **URL:** `/updatechattuple`
- **Método:** POST
- **Corpo da Solicitação:**

```json
{
    "chat_nome": "Teste1",
    "chat_ip": "192.168.1.5",
    "chat_port": "8005"
}
```

### Buscar as informações de um Chat

- **URL:** `/updatechattuple`
- **Método:** POST
- **Corpo da Solicitação:**

```json
{
    "chat_nome": "TesteServer"
}
```
- **A solicitação acima deve estar criptografada no formato:**
```json
{
    "data": "JSON acima criptografado",
    "client_public_key": "Chave pública do cliente"
}
```

### Buscar a chave pública do servidor

- **URL:** `/connection`
- **Método:** POST
- **Corpo da Solicitação:**

```json
Envio sem body
```

### Verificar o status do servidor

- **URL:** `http://127.0.0.1:5000`
- **Método:** GET
- **Corpo da Solicitação:**

```json
Envio sem body
```

## Referências:

- [Flask](https://flask.palletsprojects.com/en/2.3.x)
- [Python - Microsoft Azure](https://learn.microsoft.com/pt-br/azure/app-service/quickstart-python?WT.mc_id=azuretipslatam-video-gllemos&tabs=flask%2Cmac-linux%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)
