#per elencare le istanze RDS utilizzando il comando:
aws rds describe-db-instances

# Connetti al database:
psql --host=hostname --port=port --username=username --password --dbname=database_name
# sostituisci hostname, port, username, database_name con i valori appropriati.

# Esegui una query sul database:
psql --host=hostname --port=port --username=username --password --dbname=database_name --command='select * from table_name'
# sostituisci hostname, port, username, database_name, table_name con i valori appropriati.

# Crea un backup del database:
pg_dump --host=hostname --port=port --username=username --password --dbname=database_name --format=custom --file=backup.dump
# sostituisci hostname, port, username, database_name con i valori appropriati.

# Ripristina il backup del database:
pg_restore --host=hostname --port=port --username=username --password --dbname=database_name --verbose backup.dump
# sostituisci hostname, port, username, database_name con i valori appropriati.

# Crea un nuovo database:
createdb --host=hostname --port=port --username=username --password --owner=ownername newdatabase
# sostituisci hostname, port, username, ownername, newdatabase con i valori appropriati.

# Cancella un database:
dropdb --host=hostname --port=port --username=username --password dbname
# sostituisci hostname, port, username, dbname con i valori appropriati.

# Puoi aggiungere ulteriori opzioni per filtrare l'output o visualizzare solo determinati campi. Ad esempio, puoi utilizzare il seguente comando per visualizzare solo il nome delle istanze RDS:
aws rds describe-db-instances --query 'DBInstances[].DBInstanceIdentifier' --out