import random
import datetime
import time
import slack
import os
from pathlib import Path
from dotenv import load_dotenv



env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

#opens slack app, so it's ready for me to go
os.system(os.environ['SLACK_PATH'])

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])


greetings = ["Morning everyone!", "Morning guys!", "Mooorning!", "Morning!"]

day_of_week = datetime.date.today().strftime('%A')

if day_of_week == 'Monday':
    greeting = "Morning! Hope everyone had a good weekend!"
elif day_of_week == 'Friday':
    greeting = "Morning! TGIF!"
else:
    greeting = random.choice(greetings)

# makes time post between 1 and 6 minutes from when it's run to seem more natural
mins = random.randint(1,6)
now = time.mktime((datetime.datetime.now() + datetime.timedelta(minutes=mins)).timetuple())

client.chat_scheduleMessage(channel='#test', text=greeting, post_at=now)

