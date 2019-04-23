import unittest
from decodeLibraries import B64Encoder 
from decodeLibraries import XorMachine

class hexToB64Test(unittest.TestCase):
    def testHexToB64(self):
        self.assertEqual(B64Encoder('647cbd5361524fed6374bdc236d452d7654aabcd12').getOutput(),\
             'ZHy9U2FST+1jdL3CNtRS12VKq80S')

    def testXor(self):
        self.assertEqual(XorMachine('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965').getOutput(),\
             '746865206b696420646f6e277420706c6179')

if __name__ == '__main__':
    unittest.main()