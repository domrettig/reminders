from twilio.rest import TwilioRestClient
import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

class MessageClient(object):
  def __init__(self):
    self.twilio_number = os.environ.get('TWILIO_NUMBER')
    self.twilio_client = TwilioRestClient(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))

  def send_message(self, body, to):
    self.twilio_client.messages.create(body=body, to=to, from_=self.twilio_number)

@sched.scheduled_job('cron',minute='0',hour='2,13,21')
def remind():
  with open(os.path.expanduser('~/reminders.txt'),'r') as f:
    lines = f.readlines()

  lines = [str(i)+': '+line for i,line in enumerate(lines)]
  body = ''.join(lines)

  client = MessageClient()
  client.send_message(body, os.environ.get('USER_PHONE_NUMBER'))

sched.start()