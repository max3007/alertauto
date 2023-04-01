#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

docker-compose -f production.yml up --build 

#     set -o errexit: questo comando indica alla shell di terminare lo script 
#     immediatamente se un comando restituisce un valore di uscita non zero. In altre parole, se un comando restituisce un errore, lo script si fermerà immediatamente.

#     set -o pipefail: questo comando indica alla shell di considerare un pipe 
#     interrotto se uno dei comandi nel pipe restituisce un valore di uscita non zero. Questo aiuta a garantire che gli errori non vengano ignorati in una pipeline.

#     set -o nounset: questo comando indica alla shell di terminare lo script 
#     immediatamente se si utilizza una variabile non definita.

#       ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto && ./docker_compose_production_up_build.sh"