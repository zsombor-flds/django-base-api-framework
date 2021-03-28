# Django rest_framework reference

## Django

#### Postgres DB Configuration
 In settings.py change the following parameter:

        DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'myproject',
                'USER': 'myuser',
                'PASSWORD': 'password',
                'HOST': 'localhost',
                'PORT': '',
        }
        }
 Start Postgres


        cd ./db
        sh ./create-volume.sh
        docker-compose up -d 

 If you want to use the default sqlite option:

                DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                        }
                }

- ### Setup


        django-admin startproject DjangoRest

        python manage.py migrate
        pythhon manage.py startapp api_test
        python manage.py createsuperuser

- ### Start development server

        python manage.py runserver

- ### Create the first token

Go to http://127.0.0.1:8000/admin, then manualy create token


- ### Sample model description

        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        date = models.DateField(auto_now_add=True)
    
