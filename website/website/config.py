# Configuration settings

from website import app

# import psycopg2
# import redis

# Secret key
app.secret_key = 'J^jkn!# 7dMfw10gdf788M/?GH78nE0'


# Logging
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(filename='/var/log/vcam/flask_error.log', maxBytes=52428800, backupCount=4)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)


# # Connect to Redis cache
# def cache_connect():
#     cache = redis.StrictRedis(host='redis')

#     return cache
