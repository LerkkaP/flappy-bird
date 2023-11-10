import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_rahamaa_oikein_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_myytyjen_lounaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_kun_maksu_riittava(self):
        syo_maukkaasti = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(syo_maukkaasti, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_kun_maksu_ei_riittava(self):
        syo_maukkaasti = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(syo_maukkaasti, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_kun_maksu_riittava(self):
        syo_edullisesti = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(syo_edullisesti, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_kun_maksu_ei_riittava(self):
        syo_edullisesti = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(syo_edullisesti, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_syo_maukkaasti_korttiosto_kun_maksu_riittava(self):
        maksukortti = self.maksukortti
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)

        self.assertEqual(maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_korttiosto_kun_maksu_ei_riittava(self):
        maksukortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

        self.assertEqual(maksukortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_korttiosto_kun_maksu_riittava(self):
        maksukortti = self.maksukortti
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)

        self.assertEqual(maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_korttiosto_kun_maksu_ei_riittava(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 

    def test_kortille_rahaa_ladattaessa_saldo_muuttuu_ja_kassa_kasvaa_ladatulla_summalla(self):
        maksukortti = self.maksukortti
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(maksukortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_rahaa_ladattaessa_negatiivinen_summa_ei_muuta_saldoa_eika_kassaa(self):
        maksukortti = self.maksukortti
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)