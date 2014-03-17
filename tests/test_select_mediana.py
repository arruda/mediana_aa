# -*- coding: utf-8 -*-
import unittest

from mediana import select_mediana


class TestSelectMediana(unittest.TestCase):

    def test_media_em_exemplo_5_elementos(self):
        s = [1, 2, 4, 10, 13]
        k = (len(s) + 1) / 2  #: 2

        mediana = select_mediana(s, k)
        self.assertEquals(mediana, 4)

    def test_media_em_exemplo_5_elementos_media(self):
        s = [1, 3, 5, 7, 9]
        k = (len(s) + 1) / 2  #: 3

        mediana = select_mediana(s, k)
        self.assertEquals(mediana, 5)

    def test_media_em_exemplo_6_elementos(self):
        # numa par ele pega o anterior ao que seria do meio

        s = [1, 2, 8, 9, 4, 10]
        k = (len(s) + 1) / 2  #: 2

        mediana = select_mediana(s, k)
        self.assertEquals(mediana, 4)

    def test_media_em_exemplo_7_elementos(self):

        s = [15, 1, 3, 5, 7, 9, 10]
        k = (len(s) + 1) / 2  #: 2

        mediana = select_mediana(s, k)
        self.assertEquals(mediana, 7)

    def test_media_em_exemplo_livro_11_elementos(self):
        s = [2, 36, 21, 5, 8, 13, 11, 20, 5, 4, 1]
        k = (len(s) + 1) / 2  #: 6

        mediana = select_mediana(s, k)
        self.assertEquals(mediana, 8)
