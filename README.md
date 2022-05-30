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

Funcionalidades do **script**:
- [x] Configurar Bot
- [x] Configurar Livechat
- [x] Configurar Departamento Padrão

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
## Extras
  Para acessar informações adicionais como, execução dos scripts e deploy na plataforma Okteto, clique nos seguintes links ou acesse a pasta chamada ["docs"](https://github.com/Leo0liveira/rocketchat-rasa/tree/main/docs)

  - [Scripts](https://github.com/Leo0liveira/rocketchat-rasa/blob/main/docs/scripts.md)
  - [Okteto](https://github.com/Leo0liveira/rocketchat-rasa/blob/main/docs/okteto.md)

---

## Desenvolvido por
- 👨‍💻 [João Paulo Wakugawa](https://github.com/jpwakugawa)
- 👨‍💻 [Leonardo Felipe Oliveira Freitas](https://github.com/Leo0liveira)
---
