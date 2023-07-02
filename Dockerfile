FROM python:3.10-alpine
WORKDIR /src
ADD *.py .
ADD requirements.txt .
ARG PROTOSPIEL_ONLINE_BOT_DISCORD_TOKEN
RUN pip install -r requirements.txt

# Actual discord bot command
CMD [ "python", "./po_regmanager.py" ]