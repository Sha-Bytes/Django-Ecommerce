# 🛒E-Commerce
<b>This is a fully functional eCommerce website for purchase Games with a beautiful user interface and backend functionalities.</b>

<br>

## Features
- User and guest checkout capabilities.
- Setting up the templates and data structure in the first two modules.
- Adding user checkout flow with payment integration.
- After complete basic checkout with a logged-in user.
- Add in the ability for users to checkout as a guest using cookies.

<br>

## Roadmap & Technologies 

| Status | Item | info | 
| --- | --- | --- |
| ✅ | **Django** | For `backend logic` |
| ✅ | **HTML** | For `frontend logic` |
| ✅ | **CSS** | For `frontend logic` |
| ✅ | **Bootstrap** | For `frontend logic` |
| ✅ | **JavaScript** | For `client-side logic` |
| ✅ | **Stripe** | For `Payment processor` via [Python Stripe Library](https://pypi.org/project/python-stripe/) |

<br>



## Demonstration
https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/bf301c40-838b-4afc-852f-f4f4eb80e517

<br>

## Preview

#### Homepage
<p align="left">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/a11e5843-05ec-4c90-b999-148a9c4cab7b">
</p>
<br>

#### Login
<p align="left">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/ce26c694-7450-4f65-aeff-82c5f3ba3d71">
</p>
<br>

#### Sign-up
<p align="left">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/8c70e2bb-f75a-48b1-8324-fdcaa4658459">
</p>
<br>

### Game Preview
<p align="left">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/5875fe8b-af6e-4198-93d5-9dbdc3a6237e">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/70679c29-4ea4-4d7d-aa72-53d21df97bc5">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/da930b1b-ad1d-4edf-b5fc-4af58652b5d3">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/a76f47c1-1dc4-493e-bb0e-bd0ea94f89f3">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/35b17cd3-1e13-488b-a5cb-48b3f8986247">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/6434749a-2782-4388-a589-699abe8dd265">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/0d7abb86-29c5-493f-b764-49a5834d772b">

</p>
<br>

### Shipping page
<p align="left">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/61379cb7-ea82-4663-aab4-23a2d46ae6d1">

</p>
<br>

### payment page
<p align="left">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/bae03702-6a00-4fd1-a585-6552c36737a7">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/34389059-3689-4b37-af1a-d9b960e25dd3">
  <img width="780" src="https://github.com/Sha-Bytes/Django-Ecommerce/assets/107455405/4b9ce7a3-363b-42a2-99d4-12d59edff9fe">

</p>
<br>

## To Run This Project
1. clone this project on your local machine,
```
git clone https://github.com/Sha-Bytes/Django-Ecommerce.git
```
2. create a virtual environment inside eCommerce folder,
```
virtualenv venv
```
3. activate virtual environment,(for windows)
```
.\venv\Scripts\activate 
```
4. install project dependencies from requirements.txt,
```
pip install -r requirements.txt
```

5. make some updations on settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'crispy_forms',
    'mathfilters',
    'crispy_bootstrap4',
]

STATIC_URL = 'static/'
# CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STRIPE_SECRET_KEY = "" # insert your own stripe secret key
STRIPE_PUBLISHABLE_KEY = "" # insert your own stripe public key
```
   
6. run project on your local machine,
```
python manage.py runserver
```
Visit  `http://localhost:8000` in your browser. The app should be up & running.

<br>

## Credits & Links

- [Django Framework](https://www.djangoproject.com/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs
