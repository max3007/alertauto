#!/bin/bash

# Variabili di configurazione per la connessione al database
POSTGRES_HOST='alertauto.chlolw6d5fko.eu-central-1.rds.amazonaws.com'
POSTGRES_PORT='5432'
POSTGRES_DB='alertauto'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='fb6WWAEBxeRKhyKZr1Gt'

# Impostare la data e l'ora per il nome del file di backup
DATETIME=$(date +%Y%m%d_%H%M%S)

# Impostare il percorso del file di backup
BACKUP_FILE="alertauto_backup_$DATETIME.dump"

# Eseguire il comando di backup utilizzando le variabili di configurazione
#PGPASSWORD=fb6WWAEBxeRKhyKZr1Gt pg_dump --host="$POSTGRES_HOST" --port="$POSTGRES_PORT" --username="$POSTGRES_USER" --dbname="$POSTGRES_DB" > $BACKUP_FILE
PGPASSWORD=fb6WWAEBxeRKhyKZr1Gt pg_dump --verbose --clean --no-acl --no-owner -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB -f $BACKUP_FILE

# Controllo degli errori e output della grandezza del file
if [ "$?" -eq 0 ]
then
  echo "Il backup del database $POSTGRES_DB è stato completato con successo e salvato in $BACKUP_FILE"
  echo "La grandezza del file è $(du -sh $BACKUP_FILE | awk '{print $1}')"
else
  echo "Si è verificato un errore durante il backup del database $POSTGRES_DB"
fi
