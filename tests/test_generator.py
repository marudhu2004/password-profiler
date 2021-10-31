import unittest
import os
from password_profiler.generator import *
from util import check_file

class TestNextPass(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()        
    
    def test_increment_one_char(self):

        # Checking for one char increment
        current_pass = "hello"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass)
        self.assertEquals(result, 'hellp')

    def test_one_carry(self):
        
        # Checking for one char carry
        current_pass = "hellz"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass)
        self.assertEquals(result, 'helma')

    def test_multiple_carry(self):

        # Dealing with multiple carries
        current_pass = "hezzz"
        char_set = alpha
        result = self.generator.next_pass(len(current_pass) - 1, current_pass)
        self.assertEquals(result, 'hfaaa')

    def test_add_new_char(self):

        # Dealing with addition of new character
        current_pass = "zzzz"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass)
        self.assertEquals(result, 'aaaaa')


class TestCreateWordList(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()

    def test_fixed_len_passwords(self):

        # Creating the wordlist
        self.generator.create_word_list('tests/out.txt')
        
        # Checking if the wordlist is properly generated
        check_file(self, 'tests/out.txt', 'tests/wordlists/same_length.txt')
    
    def test_varying_len_passwords(self):

        # Creating the wordlist
        self.generator.max_len = 4
        self.generator.create_word_list('tests/out.txt')
        
        # Checking if the wordlist is properly generated
        check_file(self, 'tests/out.txt', 'tests/wordlists/varying_lengths.txt')

    def test_specific_charset(self):

        # Creating the wordlist
        generator = PasswordGenerator(char_set='1234')
        generator.create_word_list('tests/out.txt')

        # Checking if the wordlist is properly generated
        check_file(self, 'tests/out.txt', 'tests/wordlists/specific_charset.txt')

    def tearDown(self):
        path = os.path.join(os.getcwd(), 'tests/out.txt')
        
        # Deleting if the output file exists
        if os.path.exists(path):
            os.remove(path)


class TestWithKnownChars(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()

    def test_base_case(self):

        # Generating the password list
        self.generator.with_known_chars("m~ax~~", '~', 'out.txt')

        # Checking if its as expected
        check_file(self, 'out.txt', 'tests/wordlists/base_substitution_case.txt')

    def test_no_char_to_substitute(self):
        with self.assertRaises(ValueError):
            self.generator.with_known_chars("hello", '~', 'out.txt')
    
    def test_symbol_in_charset(self):
        with self.assertRaises(ValueError):
            self.generator.with_known_chars("helloa", 'a', 'out.txt')