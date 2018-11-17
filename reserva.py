from bs4 import BeautifulSoup
from datetime import datetime
import icalendar

def convertir_a_data(string):
  return datetime.strptime(string,"%d/%m/%Y - %H:%M")

def convertir_reserves_a_ics(url):
  cal=icalendar.Calendar()
  cal.add('prodid', '-//reservarecursos2ics//')
  cal.add('version', '1.0')

  with open(url) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

  for tr in soup.find_all("tr"):
    if tr.find("td",class_='views-field-title'):
      titol=tr.find("td",class_='views-field-title').text.strip()
      inici=tr.find("td",class_='views-field-start-date').text.strip()
      fi=tr.find("td",class_='views-field-end-date').text.strip()
      event = icalendar.Event()
      event.add('title',titol)
      event.add('dtstart',convertir_a_data(inici))
      event.add('dtend',convertir_a_data(fi))
      cal.add_component(event)
  return cal.to_ical()

