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
    
    def test_with_masks_increment(self):

        # Dealing with mask based increment
        current_pass = "aaadd"
        mask = "!!!^^"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass, mask, mapping={'!': 'abc', '^':'def'})
        self.assertEquals(result, 'aaade')

    def test_with_mask_carry(self):

        # Dealing with mask based increment
        current_pass = "aaadf"
        mask = "!!!^^"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass, mask, mapping={'!': 'abc', '^':'def'})
        self.assertEquals(result, 'aaaed')
    
    def test_with_mask_carry_between_symbols(self):

        # Dealing with mask based increment
        current_pass = "aaaff"
        mask = "!!!^^"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass, mask, mapping={'!': 'abc', '^':'def'})
        self.assertEquals(result, 'aabdd')

    def test_with_mask_add_char(self):

        # Dealing with mask based increment
        current_pass = "cccff"
        mask = "!!!^^"
        result = self.generator.next_pass(len(current_pass) - 1, current_pass, mask, mapping={'!': 'abc', '^':'def'})
        self.assertEquals(result, 'aaaadd')

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
