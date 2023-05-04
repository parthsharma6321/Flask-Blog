import os
# postgresql://flask_blog_database_5o4g_user:nAIRRbaApebexSUInLoRJWTxNWuIIo1E@dpg-cha296m7avj5o4b0vm5g-a.singapore-postgres.render.com/flask_blog_database_5o4g
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_2')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

