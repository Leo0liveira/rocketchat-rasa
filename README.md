<h1 align="center">Rocket.Chat-Rasa</h1>
<h3 align="center">
Passo a passo de como realizar uma integração do Rocket.Chat com Rasa.
</h3>
<p align="center">
<img src = https://img.shields.io/badge/RASA-Chatbot-blueviolet>
<img src = https://img.shields.io/badge/Rocket.Chat-Canal-red>
<img src = https://img.shields.io/badge/NLP-Machine%20learning-blue>
<img src = https://img.shields.io/badge/Python-Linguagem%20-brightgreen>
</p>


---
<img align="right" height="230" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png" alt="An image of Sara, the Rasa mascot bird, holding a flag that reads Open Source with one wing, and a wrench in the other" title="Rasa Open Source">

## 1. Setup - [Rasa](https://rasa.com/docs/rasa/) 
### 1.1 Configuração do Bot
* Configure o `credentials.yml` de acordo com o bot criado no passo 2.3
  ```sh
  rocketchat:
    user: "rasa_bot"
    password: "rasa_bot"
    server_url: "http://rocketchat:3000"
  ```
 
### 1.2 Configuração do Actions
* Configure o `endpoints.yml` de acordo com seu ambiente
  ```sh
  # Configuração para ambiente docker
  action_endpoint:
    url: "http://actions:5055/webhook"

  # Configuração para ambiente local
  action_endpoint:
    url: "http://localhost:5055/webhook"
  ```

---
<p align="center">
<img src = https://img.shields.io/badge/Rocket.Chat-F5455C?style=for-the-badge&logo=rocket.chat&logoColor=white>
</p>

## 2. Setup - [Rocket.Chat](https://developer.rocket.chat/) 
### 2.1 Acessando a aplicação 
* Subindo os containers
  ```sh 
  docker-compose up -d mongo
  docker-compose up -d mongo-init-replica
  docker-compose up -d rocketchat
  ```

* Acessando os logs
  ```sh
  docker-compose logs -f mongo
  docker-compose logs -f rocketchat
  ```

Acesse http://localhost:3000/ 

### 2.2 Configuração do Workspace 
```
Username: boss
Password: boss
Server Mode: Standalone
```

### 2.3 Configuração do Bot 
Siga **Administration** > **Users** > **+ New**.
```
Name: Rasa Chatbot 
Username: rasa_bot
Email: rasa_bot@email.com
Password: rasa_bot
Roles: bot
```

Ou execute o **script**.
```sh
python3 scripts/config_env.py
```

### 2.4 Configuração do WebHook
Siga **Administration** > **Integrations** > **+ New** > **Outgoing**.
```
Event Trigger: Message Sent
Enabled: true
Name: Rasa WebHook 
Channel: #general
URLs: http://bot:5005/webhooks/rocketchat/webhook
Post as: rasa_bot
```

Siga **Advanced Settings**.
```
Retry Failed Url Calls: false
```
---
## 3. Setup - [Okteto](https://www.okteto.com/)
### 3.1 Acessando a aplicação 

  Navegue até a branch denonimada "Okteto" por meio do comando:
```
$ git checkout okteto
```
 Onde possui as configurações necessárias para realizar o deploy da aplicação no okteto, são elas:   
No arquivo `endpoints.yml` deve-se substituir o link presente pelo equivalente gerado no okteto, exemplo: 
```
action_endpoint:
  url: "https://link-gerado-pelo-okteto.cloud.okteto.net/webhook"
```
No arquivo `credentials.yml`substituir, novamente, o url presente por:
```
server_url: 
  "https://link-gerado-pelo-okteto/webhooks/rocketchat/webhook"
```
* Detalhe: Este link é o nome do serviço descrito no `docker-compose.yml` seguido por seu "-usuário.cloud.okteto.net"

Por fim, execute o comando:
```
okteto stack deploy --build
```
Abra o link que será gerado no site do próprio okteto, ele será parecido com este, sendo que a única diferença será o nome do usuário presente no link.
* https://rocketchat-leo0liveira.cloud.okteto.net/
---
