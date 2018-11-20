import unittest
import reservarecursos

class TestReserva(unittest.TestCase):

    def test_convertir_reserves_a_ics(self):
        ics_esperat = open("test1.ics", "r").read()
        json = open("test1.json", "r").read().replace('\\','')
        ics = reservarecursos.convertir_reserves_a_ics_per_json(json)
        self.assertEquals(ics,ics_esperat)

if __name__ == '__main__':
    unittest.main()

