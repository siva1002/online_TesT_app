import random
from twilio.rest import Client
from django.conf import settings
class OtpGeneration:
    def __init__(self,phone):
        self.phone=phone
        self.otp=random.randint(11111,99999)
    def generate_otp(self):
        client = Client(settings.ACCOUNTS_SID, settings.AUTH_TOKEN)
        message = client.messages.create(
            body=f'Your otp for register{self.otp}',
            to=self.phone,
            from_="+15017250604")
        print(message.sid)