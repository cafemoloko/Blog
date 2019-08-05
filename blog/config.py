import os


class Config:
    SECRET_KEY = '240f9d742b00c6f0777a9fc3ae2b2a7b' #in python shell: import secrets | secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')