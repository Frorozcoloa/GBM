import unittest
from src.first_point.palindrome import is_palindrome, normalize


class TestPalindrome(unittest.TestCase):

    def test_normalize_spanish(self):
        """Test the normalize function with Spanish text."""
        self.assertEqual(normalize('cuya sílaba tónica es la última'), 'cuyasilabatonicaeslaultima')
        self.assertEqual(normalize('cuyasilabatonicaeslaultima'), 'cuyasilabatonicaeslaultima')
        self.assertEqual(normalize('CuyAsilÁ baTÓnicÁesla Ultimá'), 'cuyasilabatonicaeslaultima')
        self.assertEqual(normalize('!!!cuyasilabatonicaeslaultima...=='), 'cuyasilabatonicaeslaultima')

    def test_normalize_english(self):
        """Test the normalize function with English text."""
        self.assertEqual(normalize("It's a Palindrome"), 'itsapalindrome')
        self.assertEqual(normalize('it\'s a palindrome'), 'itsapalindrome')
        self.assertEqual(normalize("It's a beautiful day outside. Birds are singing, flowers are blooming. It's a perfect time for a picnic in the park!"), 'itsabeautifuldayoutsidebirdsaresingingflowersarebloomingitsaperfecttimeforapicnicinthepark')

    def test_is_palindrome_engish(self):
        """Test the is_palindrome function with English text."""
        self.assertTrue(is_palindrome('civic'))
        self.assertTrue(is_palindrome('deified'))
        self.assertTrue(is_palindrome('deleveled'))
        self.assertTrue(is_palindrome('detartrated'))
        self.assertTrue(is_palindrome('devoved'))
        self.assertTrue(is_palindrome('dewed'))
        self.assertTrue(is_palindrome('Step on no pets'))
        self.assertTrue(is_palindrome("A Toyota’s a Toyota."))
        self.assertTrue(is_palindrome("Lewd did I live, & evil I did dwel"))

    def test_not_palindrome_english(self):
        """Test the is_palindrome function with English text."""
        self.assertFalse(is_palindrome('Alice in Wonderland'))
        self.assertFalse(is_palindrome('The quick brown fox jumps over the lazy dog'))

    def test_is_palindrome_spanish(self):
        """Test the is_palindrome function with Spanish text."""
        self.assertTrue(is_palindrome('anÏtá lavA la tina'))
        self.assertTrue(is_palindrome('A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá'))
        self.assertTrue(is_palindrome('DÄbale arrÓZ a la zorra el abÄD'))
        self.assertTrue(is_palindrome('A ti no, bonita'))
        self.assertTrue(is_palindrome('A la catalana banal, atácala'))

    def test_not_palindrome_spanish(self):
        """Test the is_palindrome function with Spanish text."""
        self.assertFalse(is_palindrome('El rápido zorro marrón salta sobre el perro perezoso'))
        self.assertFalse(is_palindrome('Alicia en el país de las maravillas'))


    def test_palidrome_in_french(self):
        """Test the is_palindrome function with French text."""
        self.assertTrue(is_palindrome('Engage le jeu que je le gagne'))
        self.assertTrue(is_palindrome('Esope reste ici et se repose'))
        self.assertTrue(is_palindrome('Esope repose'))

if __name__ == '__main__':
    unittest.main()
