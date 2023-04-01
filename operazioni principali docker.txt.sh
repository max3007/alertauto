# Ecco alcune istruzioni di Docker con esempi di comandi:

docker run
# : Avvia un nuovo container basato sull'immagine specificata.
# Esempio: docker run hello-world

docker build
# : Crea un'immagine a partire da un file Dockerfile.
# Esempio: docker build -t myapp .

docker images
# : Elenco di tutte le immagini disponibili localmente.

docker container ls 
# per visualizzare i container in esecuzione e ottenere il loro ID
docker container inspect <container-id>
#per ottenere maggiori informazioni sul container, inclusi i dati sulle immagini utilizzate
docker container top <container-id>
#per visualizzare i processi in esecuzione all'interno del container e le immagini utilizzate da ogni processo.

docker ps
# : Elenco di tutti i container in esecuzione.

docker stop
# : Ferma un container in esecuzione.
# Esempio: docker stop my-container

docker rm
# : Rimuove un container.
# Esempio: docker rm my-container
docker images -q | xargs docker rmi
# Questo comando rimuoverà tutte le immagini non in esecuzione di Docker in modo ricorsivo, 
# quindi assicurati di non rimuovere involontariamente immagini importanti.

# Questo comando rimuoverà tutte le immagini spazzatura 
docker rmi $(docker images -f "dangling=true" -q)

docker exec
# : Esegue un comando all'interno di un container in esecuzione.
# Esempio: docker exec -it my-container bash

docker push
# : Carica un'immagine su un registry.
# Esempio: docker push myregistry/myimage

docker pull
# : Scarica un'immagine dal registry.
# Esempio: docker pull myregistry/myimage

docker-compose
# : Avvia più container come un'applicazione unica, utilizzando un file di composizione YAML.
# Esempio: docker-compose up

docker network
# : Gestisce le reti di Docker.
# Esempio: docker network create my-network

docker login
# : Effettua il login ad un registry.
# Esempio: docker login myregistry

docker tag
# : Assegna un tag ad un'immagine esistente.
# Esempio: docker tag myimage myregistry/myimage:1.0

docker inspect
# : Restituisce informazioni dettagliate su un container o un'immagine.
# Esempio: docker inspect my-container

docker commit
# : Crea un'immagine a partire da un container modificato.
# Esempio: docker commit my-container myimage:1.0

docker volume
# : Gestisce i volumi di Docker.
# Esempio: docker volume create my-volume

# alcune delle istruzioni principali di Docker Compose:

docker-compose up
# : Avvia l'applicazione, creando e avviando tutti i container definiti nel file Compose.
# Esempio: docker-compose up

docker-compose down
# : Arresta e rimuove i container, le reti e i volumi creati da docker-compose up.
# Esempio: docker-compose down

docker-compose ps
# : Elenco dei container attualmente in esecuzione come parte dell'applicazione Compose.
# Esempio: docker-compose ps

docker-compose build
# : Costruisce o ricostruisce i servizi definiti nel file Compose.
# Esempio: docker-compose build

docker-compose logs
# : Visualizza i log dei servizi in esecuzione.
# Esempio: docker-compose logs

docker-compose exec
# : Esegue un comando all'interno di un container in esecuzione.
# Esempio: docker-compose exec webserver ls -l /app

docker-compose restart
# : Riavvia i container in esecuzione.
# Esempio: docker-compose restart

docker-compose pull
# : Scarica le nuove immagini dai registries.
# Esempio: docker-compose pull

docker-compose up --build
# : Avvia l'applicazione, ricostruendo i container quando si apportano modifiche al file Compose o alle immagini.
# Esempio: docker-compose up --build

docker-compose up --detach
# : Avvia l'applicazione in background e stampa i nomi dei container.
# Esempio: docker-compose up --detach

docker-compose up --force-recreate
# : Ricrea i container anche se i loro image non sono cambiati.
# Esempio: docker-compose up --force-recreate

docker-compose up --remove-orphans
# : Rimuove i container senza definizione nel file Compose.
# Esempio: docker-compose up --remove-orphans

docker-compose down -v
# : Rimuove i container, le reti e i volumi creati da docker-compose up, inclusi i volumi.
# Esempio: docker-compose down -v

docker-compose ps -a
# : Elenco di tutti i container creati da Compose, non solo quelli in esecuzione.
# Esempio: docker-compose ps -a

docker-compose logs -f
# : Visualizza in tempo reale i log dei servizi in esecuzione.
# Esempio: docker-compose logs -f

docker-compose config
# : Verifica la validità del file Compose e visualizza il risultato della fusione.
# Esempio: docker-compose config

docker-compose scale
# : Scala un servizio a un numero specifico di istanze.
# Esempio: docker-compose scale webserver=3

docker-compose pause
# : Sospende tutti i container di un servizio.
# Esempio: docker-compose pause webserver

docker-compose unpause
# : Riprende tutti i container di un servizio sospeso.
# Esempio: docker-compose unpause webserver


# Ecco i passi principali per configurare e utilizzare Docker per il pull e il push delle immagini su un server Linux:

# Installare Docker sul server Linux:
# Per prima cosa, assicurati che Docker sia installato sul tuo server Linux. Puoi installare Docker utilizzando il gestore di pacchetti della tua distribuzione Linux, ad esempio apt-get su Ubuntu o yum su CentOS.

# Creare un account Docker Hub:
# Se non ne hai già uno, crea un account Docker Hub. Questo ti permetterà di caricare le tue immagini in Docker Hub o in un registry privato.

# Effettuare l'accesso a Docker Hub:
# Dopo aver creato l'account, accedi a Docker Hub utilizzando il comando docker login. Inserisci le tue credenziali Docker Hub quando richiesto.

# Creare una nuova immagine Docker:
# Per creare una nuova immagine Docker, crea un Dockerfile nella tua directory di lavoro. Il Dockerfile descrive come costruire l'immagine Docker. Utilizza il comando docker build per costruire l'immagine.

# Taggare l'immagine Docker:
# Per caricare l'immagine su Docker Hub, è necessario taggarla con il nome del registry. Usa il comando docker tag per farlo.

# Caricare l'immagine Docker su Docker Hub:
# Utilizza il comando docker push per caricare l'immagine su Docker Hub. Assicurati di specificare il nome dell'immagine con il tag corretto.

# Scaricare un'immagine Docker dal registry:
# Utilizza il comando docker pull per scaricare un'immagine Docker dal registry. Assicurati di specificare il nome dell'immagine con il tag corretto.

# Questi sono solo i passaggi di base per configurare e utilizzare Docker per il pull e il push delle immagini su un server Linux. Ci sono molti altri comandi e opzioni disponibili in Docker per lavorare con le immagini e i registry. La documentazione ufficiale di Docker offre una guida completa a tutte le funzionalità di Docker.

# Puoi utilizzare il comando 
docker container ls 
#per visualizzare i container in esecuzione e ottenere il loro ID. Poi, utilizzando l'ID del container, puoi eseguire il comando docker 
container inspect <container-id> 
#per ottenere maggiori informazioni sul container, inclusi i dati sulle immagini utilizzate.
# In alternativa, puoi eseguire il comando 
docker container top <container-id> 
#per visualizzare i processi in esecuzione all'interno del container e le immagini utilizzate da ogni processo.

docker images -q | xargs docker rmi
# Questo comando rimuoverà tutte le immagini non in esecuzione di Docker in modo ricorsivo, 
#quindi assicurati di non rimuovere involontariamente immagini importanti.