#!/usr/bin/env python3

import hug
from urllib import parse

import falcon
import pathlib

ALIASES = pathlib.Path('aliases')

data = {}
RESPONSE_TEMPLATE = '''
<html>
  <head><title>putongwords.com</title></head>
  <body><a href="{destination}">moved here></a</body>
</html>
'''


def find(shortlink):
    """
    Searches the linkdata for the golink. Returns empty dict if not found
    """
    return data.get(shortlink, {})


@hug.sink('/')
def redirect_handler(request, response):
    """Main shortlink handler"""

    shortlink = request.path.lstrip('/')

    link = find(shortlink)

    if request.method == 'GET' and link:
        return redirect(response, link['destination'])
    else:
        pass


def redirect(response, destination):
    """
    Use 301 to redirect regular URLs
    """

    url = parse.urlparse(destination)

    if not url.scheme:
        fulldestination = "https://%s" % destination
    else:
        fulldestination = destination

    #response.status = falcon.HTTP_301
    response.status = falcon.HTTP_302
    response.set_header('Location', fulldestination)
    response.set_header('Cache-Control', 'private, max-age=90')

    response.content_type = falcon.MEDIA_HTML
    response.body = RESPONSE_TEMPLATE.format(destination=fulldestination)


def read_db():
    """
    Reads all linkdata from the file
    """

    # Convert the following format into server format
    # Input
    #   g google.com
    #
    # Output
    #  [{'shortlink': 'g', 'destination': 'google.com'}]
    #
    lines = filter(None, ALIASES.read_text().split('\n'))

    for line in lines:
        [shortlink, destination] = line.split(' ')

        # root path "/" is internally represented as ""
        if shortlink == '/':
            shortlink = ''

        data[shortlink] = {'shortlink': shortlink, 'destination': destination}


@hug.startup()
def setup(api):
    """
    Read the database when server boots up
    """
    read_db()
