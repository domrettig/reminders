from bottle import post, request, response, route, run
from twilio import twiml
from update import update

class BadInput(Exception):
  pass

@route('/')
def check():
    return 'Working!'

@post('/twilio')
def inbound_sms():
    inbound_message = request.forms.get('Body')
    try:
      operation = inbound_message.split(' ')[0]
      if operation == 'add':
        text = inbound_message.split(' ')[1:]
        if not text:
          raise BadInput
        update(operation, text=text)
      else:
        num = int(inbound_message.split(' ')[1])
        update(operation, num=num)
    except IndexError, BadInput:
      twiml_response = twiml.Response()
      twiml_response.message('Bad input. Try again.')
      response.content_type = 'application/xml'
      return str(twiml_response)

if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, reloader=True)
