# [Receipt_digitalization]



## Quick Start in [Docker](https://www.docker.com/)

> Get the code

```bash
$ git clone https://github.com/app-generator/django-datta-able.git
$ cd django-datta-able
```

> Start the app in Docker

```bash
$ docker-compose pull   # download dependencies 
$ docker-compose build  # local set up
$ docker-compose up -d  # start the app 
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

![Datta Able Django - Open-source seed project crafted in Django](https://user-images.githubusercontent.com/51070104/141156910-d6a7eeba-d7a5-499b-a766-2066efd5f6b6.gif)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-datta-able.git
$ cd django-datta-able
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port 
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and **create a new user**. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

### [Django Admin Dashboards](https://appseed.us/admin-dashboards/django)

Index with UI-ready **admin dashboards** generated by the AppSeed platform in [Django Framework](https://www.djangoproject.com/).
Start fast your next Django project by using functional admin dashboards enhanced with Database, ORM, authentication flow, helpers and deployment scripts.

<br />

### [What is Django](https://docs.appseed.us/content/what-is/django)

[Django](https://www.djangoproject.com/) is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.

<br />

### [What is a dashboard](https://en.wikipedia.org/wiki/Dashboard_(business))

A dashboard is a set of pages that are easy to read and offer information to the user in real-time regarding his business. A dashboard usually consists of graphical representations of the current status and trends within an organization. Having a well-designed dashboard will give you the possibility to act and make informed decisions based on the data that your business provides - *definition provided by [Creative-Tim - Free Dashboard Templates](https://www.creative-tim.com/blog/web-design/free-dashboard-templates/?ref=appseed)*.

<br />

### Datta Able Free Dashboard

Datta Able Bootstrap Lite is the most styled Bootstrap 4 Lite Admin Template, around all other Lite/Free admin templates in the market. It comes with high feature-rich pages and components with fully developer-centric code. Comes with error/bug-free, well structured, well-commented code and regularly with all latest updated code, which saves your large amount of developing backend application time and it is fully customizable. - provided by **CodedThemes**.

<br />

---
[Datta Able Django](https://appseed.us/admin-dashboards/django-datta-able) - Provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
