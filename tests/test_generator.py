import unittest
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

    def test_one_char(self):
        pass