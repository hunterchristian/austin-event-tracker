import configparser
config = configparser.ConfigParser()
config.read('../config.ini')

import sys
# Include modules in parent directory (mainly for /database folder)
sys.path.append(config['ProjectPath'])

from bs4 import BeautifulSoup

from browser import getPageSource
from formatter import createDefaultEndTime

from database.createDatabase import db
from database.models import Event

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from hashlib import sha256

db.create_all()

AUSTIN_EVENTS_URL = 'https://do512.com/'
EMPTY_DATE = '<not found>'

def scrape_events():
  soup = BeautifulSoup(getPageSource(AUSTIN_EVENTS_URL), 'html.parser')
  
  events = soup.find_all('div', class_='ds-listing event-card')

  datetime_start = EMPTY_DATE
  for event in events:
    maybe_date = event.find('meta', attrs={'itemprop': 'startDate'})
    if maybe_date:
      datetime_start = maybe_date.datetime
      datetime_end = createDefaultEndTime(datetime_start, time)

    # FIXME parse the actual time
    time = '?'
    desc = event.find(class_='ds-listing-event-title-text').get_text(strip=True)
    # FIXME parse the actual price
    price = '?'

    if datetime_start == EMPTY_DATE:
      raise Exception('Date not found for event: ' + desc)

    # Create hash of all info about this event
    # to detect duplicates in DB
    id = int(sha256((datetime_start + time + desc + price).encode('utf-8')).hexdigest(), 16) % sys.maxsize

    event = db.session.query(Event).filter_by(id=id).first()

    # TODO handle creation of 'all day' events
    if time == 'All Day':
      continue

    

    # Only add event to the DB if it doesn't already exist
    if event is None:
      event = Event(
        id=id,
        date=datetime_start,
        datetime_end=datetime_end,
        datetime_start=datetime_start,
        description=desc,
        price=price,
        time=time
      )

      db.session.add(event)
      db.session.commit()

scrape_events()