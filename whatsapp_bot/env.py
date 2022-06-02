from json import load
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.environ["SID"]
TWILIO_AUTH_TOKEN = os.environ["TOKEN"]

DJANGO_SECRET_KEY = os.environ["SECRET_KEY"]