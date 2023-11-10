import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_raha_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo, 800)

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_jos_rahat_riittivat_palauta_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_jos_rahat_ei_riittanyt_palauta_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test_saldo_euroina_palauttaa_saldon_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_str_palauttaa_oikean_tekstin(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    