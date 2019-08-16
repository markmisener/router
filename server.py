""" starts the flask app """

import os
from flask import Flask, request, render_template


# configure flask app
app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE', silent=True)
MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN', None)

# display at homepage path
@app.route('/')
def display():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    return render_template('index.html',
                           origin=origin,
                           destination=destination,
                           MAPBOX_ACCESS_TOKEN=MAPBOX_ACCESS_TOKEN)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
