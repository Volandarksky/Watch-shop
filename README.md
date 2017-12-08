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
    │   ├── __init__.pyc
    │   ├── admin.py
    │   ├── admin.pyc
    │   ├── forms.py
    │   ├── forms.pyc
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   └── __init__.pyc
    │   ├── models.py
    │   ├── models.pyc
    │   ├── tests.py
    │   ├── urls.py
    │   ├── urls.pyc
    │   ├── views.py
    │   └── views.pyc
    ├── manage.py
    ├── orders
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── admin.py
    │   ├── admin.pyc
    │   ├── context_processors.py
    │   ├── context_processors.pyc
    │   ├── models.py
    │   ├── models.pyc
    │   ├── tests.py
    │   ├── urls.py
    │   ├── urls.pyc
    │   ├── views.py
    │   └── views.pyc
    ├── products
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── admin.py
    │   ├── admin.pyc
    │   ├── models.py
    │   ├── models.pyc
    │   ├── tests.py
    │   ├── urls.py
    │   ├── urls.pyc
    │   ├── views.py
    │   └── views.pyc
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
    │   │       ├── 11.jpg
    │   │       ├── 12.jpg
    │   │       ├── 13.jpg
    │   │       ├── 1_1YBp5l0.jpg
    │   │       ├── 1_2e8nm9v.jpg
    │   │       ├── 1_KfdddFo.jpg
    │   │       ├── 1_V6cD2nH.jpg
    │   │       ├── 1_VNYDR25.jpg
    │   │       ├── 1_hExmgk0.jpg
    │   │       ├── 2.jpg
    │   │       ├── 21.jpg
    │   │       ├── 21_MJ9Wpvh.jpg
    │   │       ├── 22.jpg
    │   │       ├── 23.jpg
    │   │       ├── 23_R3GCkqf.jpg
    │   │       ├── 2_JcjJXGO.jpg
    │   │       ├── 2_WExDFNK.jpg
    │   │       ├── 2_WNBzd7b.jpg
    │   │       ├── 2_mgyTcNj.jpg
    │   │       ├── 3.jpg
    │   │       ├── 3_a1C5sgK.jpg
    │   │       ├── 3_aJ1NDaH.jpg
    │   │       ├── 4.jpg
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
        ├── __init__.pyc
        ├── settings.py
        ├── settings.pyc
        ├── urls.py
        ├── urls.pyc
        ├── wsgi.py
        └── wsgi.pyc
