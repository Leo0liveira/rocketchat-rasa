##  Setup - [Okteto](https://www.okteto.com/)
### Realizando deploy da aplicação 

O primeiro passo a ser feito é realizar o comando:
```
$ docker-compose up --build 
```
Em seguida é necessário realizar os passos documentados no readme da aplicação, ou seja:
- **1 - Acessar o link: http://localhost:3000/**
- **2 - Criar um usuário.**
- **3 - Criar o usuário bot manualmente ou por meio dos scripts.**
- **4 - Criar a Integração entre o serviço e o usuário bot.**

Feito isso, deve-se encerrar o Docker-compose (control + c )

Em seguida, acesse o arquivo docker-compose.yml e insira a seguinte diretiva, no serviço chamado "bot"

```
public: true 
```


Por fim, execute o comando:
```
okteto stack deploy --build
```
Abra o link que será gerado no site do próprio okteto, ele será parecido com este, sendo que a única diferença será o nome do usuário presente no link.
* https://rocketchat-leo0liveira.cloud.okteto.net/
---
