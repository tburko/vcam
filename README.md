# vcam
Garage48 Vegetation Camera Project


# Start gunicorn to run web app
gunicorn -c /home/vcam/vcam/website/gunicorn.py.ini run:app


# Nginx web server
Configuration files need to go in the following locations:
/etc/nginx/nginx.conf
/etc/nginx/conf.d/vcam.conf

Delete the default configuration:
/etc/nginx/conf.d/default.conf


## Links

[picamera](http://picamera.readthedocs.io/en/release-1.12/)
