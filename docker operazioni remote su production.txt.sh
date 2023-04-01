
# build django
ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto && ./docker_compose_build_django.sh"< /dev/null

# build production
ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto && ./docker_compose_production_build.sh"< /dev/null

# up and build
ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto && ./docker_compose_production_up_build.sh"< /dev/null

# up
ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto && ./docker_compose_production_up.sh"< /dev/null

ssh -i "~/alertauto.pem" ubuntu@35.158.51.202 "cd /home/ubuntu/alertauto/backup/ && ./postresql_backup.sh"< /dev/null