FROM rasa/rasa:3.1.0-full

USER root

WORKDIR /bot
COPY ./bot /bot

RUN rasa train 

USER 1001

ENTRYPOINT []
CMD []