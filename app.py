import os
import datetime
from flask import Flask
from app import create_app
from config import config_by_name


env = os.getenv('APP_ENV') or 'dev'
app = create_app(env)


@app.route('/')
def hello():
    return 'My App!'


@app.route('/ping')
def ping():
    return datetime.datetime.now().isoformat()


@app.route('/version')
def version():
    return config_by_name[env].VERSION


@app.route('/healthz')
def healthz():
    return 'Ok'


if __name__ == '__main__':
    app.run()
