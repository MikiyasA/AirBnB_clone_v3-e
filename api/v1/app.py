#!/usr/bin/python3
"""
Status of your API
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """ method to handle @app.teardown_appcontext
    that calls storage.close()"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """ custom handler for 404 errors that returns a
    JSON-formatted 404 status code response
    """
    return (jsonify(error="Not found"), 404)

if __name__ =="main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host ='0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if notHBNB_API_PORT else  HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)
