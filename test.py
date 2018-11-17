import unittest
import reservarecursos

class TestReserva(unittest.TestCase):

    def test_convertir_reserves_a_ics(self):
        ics=reservarecursos.convertir_reserves_a_ics("test1.json")
        self.assertEquals("""BEGIN:VCALENDAR
VERSION:1.0
PRODID:-//reservarecursos2ics//
BEGIN:VEVENT
DTSTART;VALUE=DATE-TIME:20181107T143000
DTEND;VALUE=DATE-TIME:20181107T153000
TITLE:Prueba Manel
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE-TIME:20181108T131500
DTEND;VALUE=DATE-TIME:20181108T141500
TITLE:Prova3 Jordir
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE-TIME:20181113T193000
DTEND;VALUE=DATE-TIME:20181113T210000
TITLE:Proves reserva de sales FIB
END:VEVENT
END:VCALENDAR
"""
,ics.replace('\r',''))

if __name__ == '__main__':
    unittest.main()
