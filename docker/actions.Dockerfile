FROM rasa/rasa-sdk:3.1.1

WORKDIR /bot
COPY ./bot/actions /bot/actions

USER root
USER 1001

ENTRYPOINT [./entrypoint.sh]