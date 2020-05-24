import requests
from quart import Quart
from quart.signals import request_started, request_finished

from howfast_apm import HowFastQuartMiddleware

app = Quart(__name__)

@app.route('/')
async def index():
    return 'ok'

@app.route('/name/<string:name>')
async def names(name):
    return f'ok, {name}'

@app.route('/external-call')
async def external_call():
    requests.put('https://www.howfast.tech/')
    return 'ok'

@app.route('/exception')
async def exception():
    raise Exception("Unhandled exception, kaboom!")

@app.route('/error')
async def error():
    raise SystemExit()

@app.route('/record/<int:id>')
async def records(id):
    if id <= 42:
        return 'ok'
    # Return a 404 status code
    return 'not found', 404


# Make sure HOWFAST_APM_DSN is defined and contains the app DSN
HowFastQuartMiddleware(app)

app.run()
