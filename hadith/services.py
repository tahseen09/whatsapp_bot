import random
from twilio.rest import Client

from hadith.apps import HadithConfig
from whatsapp_bot.env import TWILIO_SID, TWILIO_AUTH_TOKEN

def send_whatsapp_message(from_, to, body):
    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=body,
        from_=from_,
        to=to
    )


def get_random_hadith():
    hadiths = HadithConfig.hadiths
    hadith = random.choice(hadiths)
    return f"{hadith['En_Sanad']} \n {hadith['En_Text']}"
