FROM rasa/rasa:3.0.4-full

WORKDIR /bot
COPY ./bot /bot

USER root
USER 1001

ENTRYPOINT []
CMD []
