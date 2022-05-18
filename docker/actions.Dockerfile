FROM rasa/rasa-sdk:3.1.1

WORKDIR /app
USER root
COPY ./bot/actions /app/actions

USER 1001