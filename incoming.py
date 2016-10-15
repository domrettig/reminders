from bottle import post, request, response, route, run
from twilio import twiml

@route('/')
def check():
    return 'Working!'

@post('/twilio')
def inbound_sms():
    inbound_message = request.forms.get('Body')
    print inbound_message
    twiml_response = twiml.Response()
    twiml_response.message('Received!')
    response.content_type = 'application/xml'
    return str(twiml_response)

if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, reloader=True)
