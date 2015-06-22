# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
import datetime
import os
from eve import Eve


# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'


####################
# logic application #
####################
def after_insert_spot(items):
    print 'About to store items to "%s" ' % items
    items.append('dateCreation : Wed, 21 Nov 2012 16:04:56 GMT')
    print 'About to store items [ with dateCreation filed] to "%s" ' % items

def before_insert_spot(resource):
     print 'About resource items to "%s" ' % resource
#     resource.form('dateCreation','Wed, 21 Nov 2012 16:04:56 GMT')
     print 'About resource items to "%s" ' % resource


def post_post_spots(request):
    print 'About to store request  "%s" ' % request

# Run app
app = Eve()

#app.on_inserted_spots += after_insert_spot
app.on_insert_spots += before_insert_spot
#app.on_pre_POST_spots += post_post_spots


@app.after_request
def after_request(response):
    response.headers.add('X-Ahmed', 'Je Suis Ahmed.')
    response.headers.add('X-Charlie', 'Je Suis Charlie.')
    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host=host, port=port, debug = True)
