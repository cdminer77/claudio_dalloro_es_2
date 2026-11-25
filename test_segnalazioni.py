"""Test per le segnalazioni dei difetti riscontrati dalla segreteria."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def setUp(self):
        self.giorno = date(2026, 11, 3)
        self.agenda = Agenda()

    def test_prenotazioni_contigue_stessa_sala(self):
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        prima = Prenotazione("A2", self.giorno, "09:00", "10:00", "Mario Rossi", 5)
        seconda = Prenotazione("A2", self.giorno, "10:00", "11:00", "Anna Verdi", 5)
        self.agenda.prenota(prima, oggi=self.giorno)

        id_seconda = self.agenda.prenota(seconda, oggi=self.giorno)

        self.assertFalse(prima.si_sovrappone(seconda))
        self.assertEqual(id_seconda, 2)

    def test_prenotazione_alla_capienza_massima(self):
        self.agenda.aggiungi_sala(Sala("R1", "Sala riunioni", 10))
        richiesta = Prenotazione("R1", self.giorno, "09:00", "10:00", "Mario Rossi", 10)

        id_prenotazione = self.agenda.prenota(richiesta, oggi=self.giorno)

        self.assertEqual(id_prenotazione, 1)


if __name__ == "__main__":
    unittest.main()
