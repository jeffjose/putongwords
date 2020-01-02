#!/bin/sh

gunicorn --bind 0.0.0.0:$PORT putongwords:__hug_wsgi__
