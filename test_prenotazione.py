"""Test della classe Prenotazione."""

import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def setUp(self):
        self.giorno = date(2026, 11, 3)

    def test_orari_non_ammessi(self):
        casi = [
            ("09:15", "10:00"),
            ("08:10", "10:00"),
            ("07:30", "09:00"),
            ("19:00", "20:30"),
            ("10:00", "10:00"),
            ("10:30", "10:00"),
        ]
        for inizio, fine in casi:
            with self.subTest(inizio=inizio, fine=fine):
                with self.assertRaises(ValueError):
                    Prenotazione("A1", self.giorno, inizio, fine, "Mario Rossi", 5)

    def test_giorno_tipo_errato(self):
        for giorno_errato in ("2026-11-03", 20261103, None):
            with self.subTest(giorno=giorno_errato):
                with self.assertRaises(TypeError):
                    Prenotazione("A1", giorno_errato, "09:00", "10:00", "Mario", 5)

    def test_durata_minuti(self):
        casi = [
            ("09:00", "09:30", 30),
            ("09:00", "10:30", 90),
            ("08:00", "20:00", 720),
        ]
        for inizio, fine, attesa in casi:
            with self.subTest(inizio=inizio, fine=fine):
                prenotazione = Prenotazione(
                    "A1", self.giorno, inizio, fine, "Mario Rossi", 5
                )
                self.assertEqual(prenotazione.durata_minuti(), attesa)


if __name__ == "__main__":
    unittest.main()
