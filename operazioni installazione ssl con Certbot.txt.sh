# installazione ssl con Certbot

# Execute the following instructions on the command line on the machine to ensure that you have the latest version of snapd:
sudo snap install core; sudo snap refresh core

# If you have any Certbot packages installed using an OS package manager like apt, dnf, or yum, you should remove 
# them before installing the Certbot snap to ensure that when you run the command certbot the snap is used rather 
# than the installation from your OS package manager. The exact command to do this depends on your OS, but common 
# examples are 
sudo apt-get remove certbot
sudo dnf remove certbot
sudo yum remove certbot

# Run this command on the command line on the machine to install Certbot:
sudo snap install --classic certbot

# Execute the following instruction on the command line on the machine to ensure that the certbot command can be run:
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# get a certificate:
# edit your nginx configuration automatically to serve it, turning on HTTPS access in a single step:
sudo certbot --nginx -d alertauto.it -d www.alertauto.it

# just get a certificate:
sudo certbot certonly --nginx

# Test automatic renewal:
sudo certbot renew --dry-run

# The command to renew certbot is installed in one of the following locations:

# /etc/crontab/
# /etc/cron.*/*
# systemctl list-timers

# To confirm that your site is set up properly, visit https://yourwebsite.com/ 
# in your browser and look for the lock icon in the URL bar.