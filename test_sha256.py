import unittest
from sha256 import SHA256

class TestSHA256(unittest.TestCase):
    def test_hash(self):
        test = SHA256('hello world')
        self.assertEqual(test.digest, 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9')

if __name__ == '__main__':
    unittest.main()
    