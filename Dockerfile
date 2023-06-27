FROM python:3.10-alpine
WORKDIR /src
ADD *.py .
ADD requirements.txt .
ARG PROTOSPIEL_ONLINE_BOT_DISCORD_TOKEN
RUN pip install -r requirements.txt
#Only opened and listened to because Back4App deploy told me I needed one
#EXPOSE 80
#CMD ["python", "./fakesrv.py", "-t", "-p","80", "&"]

# Actual discord bot command
CMD [ "python", "./po_regmanager.py" ]