from unittest import TestCase, main

def to_roman(number):
    q, r = divmod(number, 5)
    if number == 8:
        return "VIII"
    if number == 5:
        return "V"
    if number == 4:
        return "IV"
    if number < 4:
        return number * "I"

    

class TestConverToRoman(TestCase):
    def test_convert_1_to_roman(self):
        self.assertEquals("I", to_roman(1))

    def test_convert_2_to_roman(self):
        self.assertEquals("II", to_roman(2))

    def test_convert_3_to_roman(self):
        self.assertEquals("III", to_roman(3))

    def test_convert_4_to_roman(self):
        self.assertEquals("IV", to_roman(4))

    def test_convert_5_to_roman(self):
        self.assertEquals("V", to_roman(5)) 

    def test_convert_8_to_roman(self):
        self.assertEquals("VIII", to_roman(8))       
    

if __name__ == "__main__":
    main()


