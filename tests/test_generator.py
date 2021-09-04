import unittest
import os
from password_profiler.generator import *


class TestNextPass(unittest.TestCase):
    
    def test_increment_one_char(self):

        # Checking for one char increment
        current_pass = "hello"
        char_set = alpha
        result = next_pass(len(current_pass) - 1, char_set, current_pass)
        self.assertEquals(result, 'hellp')

    def test_one_carry(self):
        
        # Checking for one char carry
        current_pass = "hellz"
        char_set = alpha
        result = next_pass(len(current_pass) - 1, char_set, current_pass)
        self.assertEquals(result, 'helma')

    def test_multiple_carry(self):

        # Dealing with multiple carries
        current_pass = "hezzz"
        char_set = alpha
        result = next_pass(len(current_pass) - 1, char_set, current_pass)
        self.assertEquals(result, 'hfaaa')

    def test_add_new_char(self):

        # Dealing with addition of new character
        current_pass = "zzzz"
        char_set = alpha
        result = next_pass(len(current_pass) - 1, char_set, current_pass)
        self.assertEquals(result, 'aaaaa')


class TestCreateWordList(unittest.TestCase):

    def test_specific_charset(self):

        # Creating the wordlist
        create_word_list('tests/out.txt', min_len=3, max_len=3, char_set='1234')

        # Checking if the wordlist is properly generated
        with open('tests/out.txt', 'r') as created_file:
            with open('tests/wordlists/specific_charset.txt', 'r') as case_file:
                
                # Reading the password list
                gen_pass = created_file.readline()
                test_pass = case_file.readline()

                # Checking if the passwords match
                if gen_pass == test_pass:
                    self.assertEquals(gen_pass, test_pass)


    def test_empty_charset(self):
        create_word_list('out.txt', lower=False)

        # Checking if a output file was created
        self.assertFalse(os.path.exists('tests/out.txt'))


    def tearDown(self):
        path = os.path.join(os.getcwd(), 'tests/out.txt')
        
        # Deleting if the output file exists
        if os.path.exists(path):
            os.remove(path)

