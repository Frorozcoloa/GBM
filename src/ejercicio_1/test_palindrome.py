from palindrome import is_palindrome, normalize

class TestPalindrome:
    def test_normalize_spanish(self):
        assert normalize('cuya sílaba tónica es la última') == 'cuyasilabatonicaeslaultima'
        assert normalize('cuyasilabatonicaeslaultima') == 'cuyasilabatonicaeslaultima'
        assert normalize('CuyAsilÁ baTÓnicÁesla Ultimá') == 'cuyasilabatonicaeslaultima'
        assert normalize('!!!cuyasilabatonicaeslaultima...==') == 'cuyasilabatonicaeslaultima'

    def test_normalize_english(self):
        assert normalize("It's a Palindrome") == 'itsapalindrome'
        assert normalize('it\'s a palindrome') == 'itsapalindrome'
        assert normalize("It's a beautiful day outside. Birds are singing, flowers are blooming. It's a perfect time for a picnic in the park!") == 'itsabeautifuldayoutsidebirdsaresingingflowersarebloomingitsaperfecttimeforapicnicinthepark'

    def test_is_palindrome_engish(self):
        assert is_palindrome('civic')
        assert is_palindrome('deified')
        assert is_palindrome('deleveled')
        assert is_palindrome('detartrated')
        assert is_palindrome('devoved')
        assert is_palindrome('dewed')
        assert is_palindrome('Step on no pets')
        assert is_palindrome("A Toyota’s a Toyota.")
        assert is_palindrome("Lewd did I live, & evil I did dwel")

    def test_not_palindrome_english(self):
        assert not is_palindrome('Alice in Wonderland')
        assert not is_palindrome('The quick brown fox jumps over the lazy dog')

    def test_is_palindrome_spanish(self):
        assert is_palindrome('anÏtá lavA la tina')
        assert is_palindrome('A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá')
        assert is_palindrome('DÄbale arrÓZ a la zorra el abÄD')
        assert is_palindrome('A ti no, bonita')
        assert is_palindrome('A la catalana banal, atácala')

    def test_not_palindrome_spanish(self):
        assert not is_palindrome('El rápido zorro marrón salta sobre el perro perezoso')
        assert not is_palindrome('Alicia en el país de las maravillas')

    def test_palindrome_in_french(self):
        assert is_palindrome('Engage le jeu que je le gagne')
        assert is_palindrome('Esope reste ici et se repose')
        assert is_palindrome('Esope repose')
