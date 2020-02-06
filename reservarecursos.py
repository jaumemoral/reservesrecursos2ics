import json
import dateutil.parser
import icalendar
import urllib
import ssl

from datetime import date
from dateutil.relativedelta import relativedelta

def convertir_reserves_a_ics_per_id_recurs(id):
  inici = int((date.today() + relativedelta(months=-6)).strftime('%s'))*1000
  fi = int((date.today() + relativedelta(months=+6)).strftime('%s'))*1000  
  url="https://reservarecursos.upc.edu/utgcntic/bookingliveview/json?nid=%s&start=%s&end=%s" % (id,inici,fi)
  return convertir_reserves_a_ics_per_url(url)

def convertir_reserves_a_ics_per_url(url):
  # Afegim aixo per no validar el certificat SSL (dona problemes)
  try:
    _create_unverified_https_context = ssl._create_unverified_context
  except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
  else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

  text=urllib.request.urlopen(url).read().decode().replace('\\\'','\'')
  return convertir_reserves_a_ics_per_json(text)

def convertir_reserves_a_ics_per_json(text):
  data = json.loads(text)
  cal=icalendar.Calendar()
  cal.add('prodid', '-//reservarecursos2ics//')
  cal.add('version', '1.0')


  for e in data:
      if not e['mode']=='restriction':
        event = icalendar.Event()
        event.add('title',e['title'])
        event.add('dtstart',dateutil.parser.parse(e['start']))
        event.add('dtend',dateutil.parser.parse(e['end']))
        cal.add_component(event)

  return cal.to_ical()
