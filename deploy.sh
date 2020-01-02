#!/bin/sh

wget https://raw.githubusercontent.com/jeffjose/putongwords/master/aliases -O aliases
gunicorn --bind 0.0.0.0:$PORT putongwords:__hug_wsgi__
