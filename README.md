# AlertAuto

Gestione Auto e Documenti

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy alertauto

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd alertauto
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

``` bash
cd alertauto
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

``` bash
cd alertauto
celery -A config.celery_app worker -B -l info
```

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).


## Installare Nginx:
### Aggiornare la lista dei pacchetti:

``` bash
sudo apt-get update
```
### Installare Nginx:
``` bash
sudo apt-get install nginx
```
### Verificare che Nginx sia stato installato correttamente:
``` bash
sudo systemctl status nginx
```

#### Se Nginx è in esecuzione, dovresti vedere un output simile al seguente:

 ● nginx.service - A high performance web server and a reverse proxy server
      Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
      Active: active (running) since Mon 2023-02-27 14:15:50 UTC; 20s ago
        Docs: man:nginx(8)
     Process: 22531 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Main PID: 22532 (nginx)
       Tasks: 2 (limit: 4915)
      Memory: 3.8M
      CGroup: /system.slice/nginx.service
              ├─22532 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
              └─22533 nginx: worker process


#### Aprire il firewall per consentire il traffico HTTP e HTTPS:
### (su aws creare regole di entrata nei gruppi di sicurezza)
``` bash
sudo ufw allow 'Nginx Full'
```
Questo consentirà il traffico sulla porta 80 per HTTP e sulla porta 443 per HTTPS.

Verificare che Nginx risponda correttamente al traffico HTTP e HTTPS visitando l'indirizzo IP del tuo server o il nome di dominio associato. 
Ad esempio, se l'indirizzo IP del tuo server è 1.2.3.4, puoi digitare http://1.2.3.4 o https://1.2.3.4 nella barra degli indirizzi del tuo browser. 
Dovresti vedere la pagina predefinita di Nginx.