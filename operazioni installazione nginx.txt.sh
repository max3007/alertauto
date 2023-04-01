# Per installare Nginx su Ubuntu, puoi seguire questi passaggi:

# Aggiornare la lista dei pacchetti:

sudo apt-get update

# Installare Nginx:

sudo apt-get install nginx

# Verificare che Nginx sia stato installato correttamente:

sudo systemctl status nginx


# Se Nginx è in esecuzione, dovresti vedere un output simile al seguente:

# ● nginx.service - A high performance web server and a reverse proxy server
#      Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
#      Active: active (running) since Mon 2023-02-27 14:15:50 UTC; 20s ago
#        Docs: man:nginx(8)
#     Process: 22531 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
#    Main PID: 22532 (nginx)
#       Tasks: 2 (limit: 4915)
#      Memory: 3.8M
#      CGroup: /system.slice/nginx.service
#              ├─22532 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
#              └─22533 nginx: worker process


# Aprire il firewall per consentire il traffico HTTP e HTTPS:
# (su aws creare regole di entrata nei gruppi di sicurezza)

sudo ufw allow 'Nginx Full'

# Questo consentirà il traffico sulla porta 80 per HTTP e sulla porta 443 per HTTPS.

# Verificare che Nginx risponda correttamente al traffico HTTP e HTTPS visitando l'indirizzo IP del tuo server o il nome di dominio associato. 
# Ad esempio, se l'indirizzo IP del tuo server è 1.2.3.4, puoi digitare http://1.2.3.4 o https://1.2.3.4 nella barra degli indirizzi del tuo browser. 
# Dovresti vedere la pagina predefinita di Nginx.