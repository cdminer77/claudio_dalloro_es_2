"""Test per le segnalazioni dei difetti riscontrati dalla segreteria."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def test_prenotazioni_contigue_stessa_sala(self):
        martedi = date(2026, 11, 3)
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        prima = Prenotazione("A2", martedi, "09:00", "10:00", "Mario Rossi", 5)
        seconda = Prenotazione("A2", martedi, "10:00", "11:00", "Anna Verdi", 5)
        agenda.prenota(prima, oggi=martedi)

        id_seconda = agenda.prenota(seconda, oggi=martedi)

        self.assertFalse(prima.si_sovrappone(seconda))
        self.assertEqual(id_seconda, 2)


if __name__ == "__main__":
    unittest.main()
