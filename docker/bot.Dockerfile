FROM rasa/rasa:3.1.0-full

WORKDIR /app
USER root
COPY ./bot /app

# Importante treinar o modelo dentro do container!
RUN rasa train 

USER 1001

# Deixando o container virgem
ENTRYPOINT []
CMD []