import json
from datetime import datetime
import icalendar
import urllib
import ssl

def convertir_a_data(string):
  #TODO: crec que aixo no acaba de funcionar
  return datetime.strptime(string.split("+")[0],"%Y-%m-%dT%H:%M:%S")

def convertir_reserves_a_ics(url):
  cal=icalendar.Calendar()
  cal.add('prodid', '-//reservarecursos2ics//')
  cal.add('version', '1.0')

  try:
    _create_unverified_https_context = ssl._create_unverified_context
  except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
  else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

  j=urllib.urlopen(url).read().replace('\\','')
  data = json.loads(j)
  print data

  for e in data:
      if not e['mode']=='restriction':
        event = icalendar.Event()
        event.add('title',e['title'])
        event.add('dtstart',convertir_a_data(e['start']))
        event.add('dtend',convertir_a_data(e['end']))
        cal.add_component(event)

  return cal.to_ical()

