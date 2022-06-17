
# Memories

Una pagina web dove puoi pubblicare un ricordo di un Animale, anche altro se esiste quella categoria.


## Author

- [KevinSinchi](https://github.com/RevengeBOT)


## Applicazioni Django

 - Account
 - Category
 - Comments
 - Post

## Account

Ha i campi nome, cognome, informazione personale.
Quando si registra viene registrato nel grupo Utenti che non 
ha permessi per creare le categorie e i permessi di Admin.
Puo creare post, modificare il proprio account e commentare. 

## Category

Ha i campi nome, descrizione e imagine.
Ogni post deve essere registrato ad una categoria.

## Comments

Ha i campi commento, nome, user( Account ), e tempi di creazione 
update.
Questi possono essere eliminati dal creatore del commento e dal 
proprietario del commento.

## Post

Ha i campi nome, descrizione, imagine, categorie, commenti, e tempi
di creazione e update.





## Bug

- Grafica non curata in caso manchino elementi.
- Eventuali controlli di sicurezza in caso di modifiche al codice in lato client.



## Feedback

If you have any feedback, please reach out to us at kevinjss97@gmail.com


## Run Locally

Clone the project

```bash
  git clone https://github.com/RevengeBOT/Memories.git
```

Go to the project directory

```bash
  cd Memories
```

Install dependencies with python and pip already installed 

```bash
  
  pip install –user pipenv
  pipenv install django
  pipenv install pillow
  pipenv install django-crispy-forms
  pipenv install crispy-bootstrap5
  pipenv shell
```

Start the server

```bash
  python manage.py runserver
```

