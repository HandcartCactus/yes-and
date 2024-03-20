from fastapi import FastAPI, Response

from random import randint

from random_strings import random_string
from random_response import random_response

app = FastAPI()

@app.get('/')
def get_root():
    return random_response()

@app.post('/')
def post_root():
    return random_response()

@app.get('/.{ext}')
def get_dotfile(ext):
    return Response(content=random_string())

@app.get('/{basename}.{ext}')
def get_file(basename, ext):
    return Response(content=f'{basename}.{ext}')

@app.get('/{p1}/')
def get_1path(p1):
    return Response(content='')

@app.get('/{p1}/{p2}/')
def get_2path(p1, p2):
    return Response(content='')

@app.get('/{p1}/{p2}/{p3}/')
def get_3path(p1, p2, p3):
    return Response(content='')

# @app.get('/.env')
# def fake_env_file():
#     return Response(content=random_string())

# @app.get('/sitemap.xml')
# def fake_sitemap_xml():
#     ...

# @app.get('/robots.txt')
# def fake_robots_txt():
#     return Response(content=random_string())

# @app.get('/favicon.ico')
# def fake_favicon_ico():
#     ... 

# @app.get('/form.html')
# def fake_form_html():
#     ...

# /upl.php
# /geoip/
# /1.php
# /bundle.js
# /files/
# /systembc/password.php
# /password.php
# /info.php
# /portal/redlion
# /.DS_Store
# /signin.php
# /.vscode/sftp.json
# MGLNDD_52.72.56.213_443
# /webui/
# /geoserver/web/
# /.git/config
# /cgi/conf.bin
# /sitemap.xml
# /robots.txt
# /favicon.ico
# /form.html
