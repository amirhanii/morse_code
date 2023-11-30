import unittest
import Code

class Testmorsecode(unittest.TestCase):
  
    def test_string_to_morse(self):
        self.assertEqual(Code.string_to_morse('AMIR'), '.-/--/../.-./')
        self.assertEqual(Code.string_to_morse('A A'), '.-/ /.-/')

    def test_morsest(self):
        self.assertEqual(Code.morsestr('./--/-'), 'EMT')
        self.assertEqual(Code.morsestr('--/ /..'), 'M I')
        

if __name__ == '__main__':
    unittest.main()
