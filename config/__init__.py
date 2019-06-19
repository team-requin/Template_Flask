import os
from datetime import timedelta

class Config:
    # db name
    SERVICE_NAME = 'SERVICE_NAME'

    APP_HOST = '0.0.0.0'
    APP_PORT = 80
    APP_DEBUG = True

    # This setting for DB
    #
    # DB_HOST = '127.0.0.1'
    # DB_PORT = '12345'
    #

    SECRET_KEY = 'SECRET_KEY'

    # This settings for Auth
    #
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    # JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    #

    RUN_SETTINGS = {
        'host': APP_HOST,
        'port': APP_PORT,
        'debug': APP_DEBUG,
    }

    # This settings for DB
    #
    # DB_SETTINGS = {
    #     'db': SERVICE_NAME,
    #     'host': DB_HOST,
    #     'port': DB_PORT,
    #     'username': None,
    #     'password': None,
    # }
    #