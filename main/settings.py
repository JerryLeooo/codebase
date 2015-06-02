# -*- coding: utf-8 -*-

from os import environ

class EnvConfigType(type):

    def __getattribute__(cls, key):
        value = object.__getattribute__(cls, key)
        env = environ.get(key)
        if env:
            value = type(value)(env)
        return value

class Config(object):

    __metaclass__ = EnvConfigType

    DEBUG = True
    SECRET_KEY = '53a01e6bd34caef997eed24f5ee9d3e0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        environ.get('PG_USER', 'tutor'),
        environ.get('PG_PASSWORD', 'tttt'),
        environ.get('PG_HOST', 'localhost'),
        environ.get('PG_PORT', '5432'),
        environ.get('PG_DATABASE', 'tutor'))
    SQLALCHEMY_ECHO = False

    REDIS_URL = 'redis://%s:%s/%s' % (
        environ.get('REDIS_HOST', 'localhost'),
        environ.get('REDIS_PORT', '6379'),
        environ.get('REDIS_DATABASE', '1'),)
