# Watch-shop
***
### simple online store for sale watches
***
### Before Start:
### $ python manage.py makemigrations
### $ python manage.py migrate

### For start:
### $ python manage.py runserver
### and go to <http://127.0.0.1:8000/>

## Watch-shop tree
#### ├── README.md
#### └── watchShop
    ├── db.sqlite3
    ├── landing
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── forms.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    ├── manage.py
    ├── orders
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── context_processors.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    ├── products
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    ├── static
    │   ├── img
    │   │   ├── img.jpg
    │   │   └── img0.jpg
    │   ├── js
    │   │   └── scripts.js
    │   ├── landing.css
    │   ├── media
    │   │   └── product_img
    │   │       ├── 1.jpg
    │   │       ├── ................
    │   │       └── 4_sE3i7jz.jpg
    │   └── style.css
    ├── templates
    │   ├── base.html
    │   ├── footer.html
    │   ├── landing
    │   │   ├── home.html
    │   │   ├── landing.html
    │   │   └── product_item.html
    │   ├── navbar.html
    │   └── products
    │       └── product.html
    └── watchShop
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
