from dotenv import load_dotenv
import os

load_dotenv()

no_longer_secret = os.getenv('secret')

print(no_longer_secret)