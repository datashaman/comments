import flask
import re
import os

from dotenv import load_dotenv
load_dotenv()

def update_config_from_env(app):
    prefix = '%s_' % app.name.upper()
    for key, value in os.environ.items():
        match = re.match(r'^%s(.*)' % prefix, key)
        if match:
            app.config[match.group(1)] = value

app = flask.Flask(__name__)
update_config_from_env(app)

from . import routes
