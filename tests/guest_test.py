import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Abbie")

    def test_guest1_has_name(self):
        self.assertEqual("Abbie", self.guest1.name)

    # def test_guest1_wrong_name_fails(self):
    #     self.assertEqual("Susan", self.guest1.name)