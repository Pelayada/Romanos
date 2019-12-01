import unittest
import romanos

class RomanNumberTest(unittest.TestCase):

   def test_primero(self):
        self.assertEqual(romanos.cambiarArabigo("I"), 1)
        self.assertEqual(romanos.cambiarArabigo("V"), 5)
        self.assertEqual(romanos.cambiarArabigo("X"), 10)
        self.assertEqual(romanos.cambiarArabigo("L"), 50)
        self.assertEqual(romanos.cambiarArabigo("C"), 100)
        self.assertEqual(romanos.cambiarArabigo("D"), 500)
        self.assertEqual(romanos.cambiarArabigo("M"), 1000)

        self.assertEqual(romanos.cambiarArabigo("XVI"), 16)

        self.assertEqual(romanos.cambiarArabigo("XIIII"), 0)

        self.assertEqual(romanos.cambiarArabigo("IX"), 9)
        self.assertEqual(romanos.cambiarArabigo("IV"), 4)
        self.assertEqual(romanos.cambiarArabigo("XLIV"), 44)

        self.assertEqual(romanos.cambiarArabigo("VC"), 0)
        self.assertEqual(romanos.cambiarArabigo("LD"), 0)

        self.assertEqual(romanos.cambiarArabigo("XXL"), 0)
        self.assertEqual(romanos.cambiarArabigo("IIX"), 0)

        self.assertEqual(romanos.cambiarArabigo("IC"), 0)
        self.assertEqual(romanos.cambiarArabigo("XD"), 0)

        #self.assertEqual(romanos.cambiarArabigo("(IV)CCCXVII"), 4317)
        #self.assertEqual(romanos.cambiarArabigo("(VII)DCIX"), 7609)
        #self.assertEqual(romanos.cambiarArabigo("(IX)CDXLIV"), 9444)

        


class ArabicNumberTest(unittest.TestCase):


   def test_primero(self):
        self.assertEqual(romanos.cambiarRomano("3"), "III")
        self.assertEqual(romanos.cambiarRomano("9"), "IX")

        self.assertEqual(romanos.cambiarRomano("12"), "XII")
        self.assertEqual(romanos.cambiarRomano("17"), "XVII")

        self.assertEqual(romanos.cambiarRomano("24"), "XXIV")
        self.assertEqual(romanos.cambiarRomano("44"), "XLIV")
        self.assertEqual(romanos.cambiarRomano("87"), "LXXXVII")

        self.assertEqual(romanos.cambiarRomano("248"), "CCXLVIII")
        self.assertEqual(romanos.cambiarRomano("698"), "DCXCVIII")
        self.assertEqual(romanos.cambiarRomano("961"), "CMLXI")

        self.assertEqual(romanos.cambiarRomano("2485"), "MMCDLXXXV")
        self.assertEqual(romanos.cambiarRomano("6987"), "(VI)CMLXXXVII")
        self.assertEqual(romanos.cambiarRomano("9617"), "(IX)DCXVII")




class ArabicNumberTest2(unittest.TestCase):

   def test_primero(self):
        self.assertEqual(romanos.cambiarRomano2("2000"), "MM")
        self.assertEqual(romanos.cambiarRomano2("3000"), "MMM")

        self.assertEqual(romanos.cambiarRomano2("3800"), "MMMDCCC")
        self.assertEqual(romanos.cambiarRomano2("2300"), "MMCCC")

        self.assertEqual(romanos.cambiarRomano2("2430"), "MMCDXXX")
        self.assertEqual(romanos.cambiarRomano2("1970"), "MCMLXX")

        self.assertEqual(romanos.cambiarRomano2("1479"), "MCDLXXIX")
        self.assertEqual(romanos.cambiarRomano2("3568"), "MMMDLXVIII")

        self.assertEqual(romanos.cambiarRomano2("594"), "DXCIV")
        self.assertEqual(romanos.cambiarRomano2("356"), "CCCLVI")

        self.assertEqual(romanos.cambiarRomano2("49"), "XLIX")
        self.assertEqual(romanos.cambiarRomano2("56"), "LVI")

        self.assertEqual(romanos.cambiarRomano2("4"), "IV")
        self.assertEqual(romanos.cambiarRomano2("8"), "VIII")










if __name__ == '__main__':
    unittest.main()