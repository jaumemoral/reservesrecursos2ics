from bs4 import BeautifulSoup
from datetime import datetime

with open("test1.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for tr in soup.find_all("tr"):
    if tr.find("td",class_='views-field-title'):
        titol=tr.find("td",class_='views-field-title').text.strip()
        inici=tr.find("td",class_='views-field-start-date').text.strip()
        fi=tr.find("td",class_='views-field-end-date').text.strip()
        date_inici=datetime.strptime(inici,"%d/%m/%Y - %H:%M")
        date_fi=datetime.strptime(fi,"%d/%m/%Y - %H:%M")
        # TODO: fer l'exportacio en ICS
        print "%s / %s / %s" % (titol,date_inici,date_fi)

