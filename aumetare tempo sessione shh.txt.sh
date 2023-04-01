# Puoi utilizzare il comando ssh con l'opzione ServerAliveInterval per impostare l'intervallo di tempo desiderato (in secondi) tra i messaggi "sondaggio". Ad esempio, se #vuoi inviare un messaggio ogni 60 secondi, puoi utilizzare il seguente comando:

ssh -o ServerAliveInterval=60 user@ec2-instance

ssh -o ServerAliveInterval=60 -i "alertauto.pem" ubuntu@35.158.51.202

# In alternativa, puoi aggiungere l'opzione ServerAliveInterval al tuo file di configurazione SSH 
# (~/.ssh/config) in modo che venga applicata a tutte le connessioni SSH.

# Host *
#   ServerAliveInterval 60