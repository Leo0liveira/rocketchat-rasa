FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY ./scripts /app 

# Deixando o container virgem
ENTRYPOINT []
CMD []