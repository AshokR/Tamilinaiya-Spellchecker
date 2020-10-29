# -*- coding: utf-8 -*-

import unittest
from tamilinayavaani.from_Csharp import gpathil11, checkviku, getsample
from tamilinayavaani import checkword, check_sandhi

# spelling correction
# testlist = ['நேயர்கலே', ' ', 'நிகழ்சியைப்', ' ', 'பார்த்தீர்கலா']
# testlist = ['கன்னால்', ' ', 'பார்த்தென்']
# testlist = ['வேண்டுகிறேண்']
# testlist = ['கற்ப்பிக்கிறேன்']
# testlist = ['முன்ணணி']
# testlist = ['சறியாக', ' ', 'கன்டுபிடிக்கும்']

# sandhi
# testlist = ['இந்த', ' ', 'பெட்டியில்']
# testlist = ['கூலி', ' ', 'படை']
# testlist = ['இலக்கண', ' ', 'பிழைகளை']

# sandhi and spelling correction together

# testlist = ['சரிவர', ' ', 'சோதிக்கிரதா']


class TestSpellCheckWords(unittest.TestCase):
    def test_அ(self):
        testlist = ['கூலி', ' ', 'படை']
        expected = [[1, 'கூலிப்'], [0, 'correct'], [0, 'correct']]
        self.assertListEqual(expected, gpathil11(testlist, True, 'exe'))

    def test_ஆ(self):
        testlist = ['பிடிக்க', ' ', 'தடுமாரலாம்']
        expected = [[1, 'பிடிக்கத்'], [0, 'correct'], [1, 'தடுமாறலாம்']]
        self.assertListEqual(expected, gpathil11(testlist, True, 'exe'))

    def test_இ(self):
        testlist = ['பிடிக்க', ' ', 'தடுமாரலாம்']
        expected = [[1, 'பிடிக்கத்'], [0, 'correct'], [1, 'தடுமாறலாம்']]
        self.assertListEqual(expected, gpathil11(testlist, True, 'exe'))

    def test_ஈ(self):
        testlist = ['இறை', 'வனக்கம்']
        expected = [[0, 'correct'], [0, 'wrong']]
        self.assertListEqual( expected, gpathil11(testlist, True, 'exe') )

    def test_சொல்(self):
        self.assertTrue(checkword('வேண்டுகிறேன்', 7))
        expected=[['கிற்ப்பிக்கிறேன்', 'கிற்ப்பிக்கிறேன்'], ['முந்நநி', 'முந்ணணி', 'முண்நணி', 'முண்ணநி']]
        self.assertListEqual(expected[0],getsample("0", 'கற்ப்பிக்கிறேன்', 'கற', 'கிற'))
        self.assertListEqual(expected[1],getsample("0", 'முண்ணணி', 'ண', 'ந'))
        self.assertTrue(checkword('சரியாகக்கண்டுபிடிக்கும்', 0))
        self.assertTrue(checkviku('சரியா', 'க', "", 'ஆ', '15', 0))

    def test_முகப்பு(self):
        self.assertFalse(checkword('நேயர்கலே',0))

if __name__ == u'__main__':
    unittest.main()