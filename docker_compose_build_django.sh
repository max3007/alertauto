#!/bin/bash
docker-compose -f production.yml stop 
docker-compose -f production.yml build django
docker-compose -f production.yml  up -d 
# Questo comando rimuoverà tutte le immagini spazzatura:
docker rmi $(docker images -f "dangling=true" -q)
#     ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto && ./docker_compose_build_django.sh"