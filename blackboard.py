import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

execution = client.studio \
                  .flows('FW8935b8a1950c90180a2e0532905c9177') \
                  .executions \
                  .create(
                    to='+19082477262',
                    from_='+19084607058',
                    parameters={'name': 'Jefferson Elementary School'}
                    )

print(execution.sid)

