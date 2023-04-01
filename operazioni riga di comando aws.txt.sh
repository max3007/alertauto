# Ecco alcune delle operazioni che puoi eseguire sull'istanza AWS EC2 dalla riga di comando su OSX utilizzando l'AWS CLI:

# Elencare le istanze EC2:
aws ec2 describe-instances
# Questo comando restituisce informazioni su tutte le istanze EC2 disponibili nell'account AWS.


# Avviare un'istanza EC2:
aws ec2 run-instances --image-id <ID_ami> --instance-type <tipo_istanza> --key-name <nome_chiave> --security-group-ids <ID_gruppo_sicurezza>
# Sostituisci <ID_ami> con l'ID dell'Amazon Machine Image (AMI) che desideri utilizzare per l'istanza, <tipo_istanza> con il tipo di istanza che desideri avviare, <nome_chiave> con il nome della chiave di accesso che utilizzerai per accedere all'istanza e <ID_gruppo_sicurezza> con l'ID del gruppo di sicurezza che utilizzerai per controllare il traffico in entrata e in uscita dall'istanza.


# Fermare un'istanza EC2:
aws ec2 stop-instances --instance-ids <ID_istanza_EC2>
# Sostituisci <ID_istanza_EC2> con l'ID dell'istanza EC2 che desideri fermare.


# Riavviare un'istanza EC2:
aws ec2 reboot-instances --instance-ids <ID_istanza_EC2>
# Sostituisci <ID_istanza_EC2> con l'ID dell'istanza EC2 che desideri riavviare.


# Terminare un'istanza EC2:
aws ec2 terminate-instances --instance-ids <ID_istanza_EC2>
# Sostituisci <ID_istanza_EC2> con l'ID dell'istanza EC2 che desideri terminare.


# Creare un'immagine personalizzata (AMI) di un'istanza EC2:
aws ec2 create-image --instance-id <ID_istanza_EC2> --name <nome_AMI>
# Sostituisci <ID_istanza_EC2> con l'ID dell'istanza EC2 che desideri utilizzare per creare l'AMI e <nome_AMI> con il nome che desideri assegnare all'AMI.


# Creare un volume EBS:
aws ec2 create-volume --availability-zone <zona_disponibilità> --size <dimensione_volume>
# Sostituisci <zona_disponibilità> con la zona di disponibilità in cui desideri creare il volume EBS e <dimensione_volume> con la dimensione del volume in GB.


# Allegare un volume EBS a un'istanza EC2:
aws ec2 attach-volume --volume-id <ID_volume> --instance-id <ID_istanza_EC2> --device <nome_device>
# Sostituisci <ID_volume> con l'ID del volume EBS che desideri allegare, <ID_istanza_EC2> con l'ID dell'istanza EC2 a cui desideri allegare il volume e <nome_device> con il nome del dispositivo che desideri utilizzare per allegare il volume all'istanza.


# Creare un gruppo di sicurezza:
aws ec2 create-security-group --group-name <nome_gruppo> --description <descrizione_gruppo> --vpc-id <ID_vpc>
# Sostituisci <nome_gruppo> con il nome che desideri assegnare al gruppo di sicurezza, <descrizione_gruppo> con una descrizione del gruppo di sicurezza e <ID_vpc> con l'ID della Virtual Private Cloud (VPC) a cui desideri associare il gruppo di sicurezza.


# Aggiungere una regola di ingresso a un gruppo di sicurezza:
aws ec2 authorize-security-group-ingress --group-id <ID_gruppo_sicurezza> --protocol <protocollo> --port <porta> --cidr <CIDR>
# Sostituisci <ID_gruppo_sicurezza> con l'ID del gruppo di sicurezza a cui desideri aggiungere la regola, <protocollo> con il protocollo di rete che desideri consentire, <porta> con il numero di porta che desideri consentire e <CIDR> con il CIDR dell'indirizzo IP da cui desideri consentire l'accesso.


# Creare una chiave di accesso:
aws ec2 create-key-pair --key-name <nome_chiave> --query 'KeyMaterial' --output text > <nome_file>.pem
# Sostituisci <nome_chiave> con il nome che desideri assegnare alla chiave di accesso e <nome_file> con il nome del file in cui desideri salvare la chiave di accesso.


# Creare un bucket S3:
aws s3api create-bucket --bucket <nome_bucket> --region <regione>
# Questo comando crea un bucket S3 con il nome specificato nella regione specificata.

# Caricare un file in un bucket S3:
aws s3 cp <percorso_file> s3://<nome_bucket>/<percorso_destinazione>
# Questo comando carica il file specificato nel bucket S3 specificato.

# Scaricare un file da un bucket S3:
aws s3 cp s3://<nome_bucket>/<percorso_file> <percorso_destinazione>
# Questo comando scarica il file specificato dal bucket S3 specificato.


# Installazione del pacchetto AWS CLI:
# Per installare il pacchetto AWS CLI, apri il terminale sul tuo Mac e esegui il comando:

curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Questo scarica il pacchetto AWS CLI dal sito ufficiale di AWS e lo installa sul tuo Mac.
# Configurazione delle credenziali AWS:
# Dopo aver installato il pacchetto AWS CLI, è necessario configurare le credenziali AWS per poter eseguire le operazioni da riga di comando.
# Per farlo, apri il terminale e digita il comando:

aws configure

# Verrà richiesto di fornire le seguenti informazioni:
#     Access key ID: inserisci la tua chiave di accesso AWS
#     Secret access key: inserisci la tua chiave di accesso segreta AWS
#     Default region name: inserisci il nome della tua regione AWS predefinita
#     Default output format: scegli il formato di output predefinito

# To verify that the shell can find and run the aws command in your $PATH, use the following commands. 

which aws
aws --version

# output:
# /usr/local/bin/aws 
# aws-cli/2.10.0 Python/3.11.2 Darwin/18.7.0 botocore/2.4.5
