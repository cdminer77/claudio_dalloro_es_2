"""Test della classe Agenda."""

import unittest
from datetime import date, timedelta

from prenotazioni import (
    ORIZZONTE_GIORNI,
    Agenda,
    DataNonAmmessa,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.oggi = date(2026, 11, 5)
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A1", "Aula Magna", 60))

    def test_aggiungi_sala_codice_duplicato(self):
        duplicata = Sala("A1", "Altra sala", 20)

        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(duplicata)

    def test_sala_codice_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("X9")

    def test_prenota_date_non_ammesse(self):
        data_passata = self.oggi - timedelta(days=1)
        domenica = date(2026, 11, 8)
        oltre_orizzonte = self.oggi + timedelta(days=ORIZZONTE_GIORNI + 1)

        for giorno in (data_passata, domenica, oltre_orizzonte):
            with self.subTest(giorno=giorno):
                richiesta = Prenotazione(
                    "A1", giorno, "09:00", "10:00", "Mario Rossi", 10
                )
                with self.assertRaises(DataNonAmmessa):
                    self.agenda.prenota(richiesta, oggi=self.oggi)

    def test_prenota_accetta_data_di_oggi(self):
        richiesta = Prenotazione("A1", self.oggi, "09:00", "10:00", "Mario Rossi", 10)

        id_prenotazione = self.agenda.prenota(richiesta, oggi=self.oggi)

        self.assertEqual(id_prenotazione, 1)

    def test_prenotazione_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(999)

    def test_cancella_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(999)


if __name__ == "__main__":
    unittest.main()
