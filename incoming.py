from bottle import post, request, response, route, run
from twilio import twiml
from update import update
import re

class BadInput(Exception):
  pass

@route('/')
def check():
    return 'Working!'

@post('/twilio')
def inbound_sms():
    inbound_message = request.forms.get('Body')
    try:
      allowable_patterns = [re.compile(r'(add) ((\S+ )*(\S+))'),re.compile(r'(delete) ([0-9]+)')]
      operation = info = None
      for p in allowable_patterns:
        match = re.search(p, inbound_message)
        if match:
          operation = match.group(1)
          info = match.group(2)

      if not operation or not info:
        raise BadInput

      update(operation, info)

    except BadInput:
      twiml_response = twiml.Response()
      twiml_response.message('Bad input. Try again.')
      response.content_type = 'application/xml'
      return str(twiml_response)

if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, reloader=True)
