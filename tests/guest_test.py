import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Abbie")
        self.guest2 = Guest("Bob")
        self.guest3 = Guest("Carol")
        self.guest4 = Guest("Dave")
        self.guest5 = Guest("Emma")
        self.guest6 = Guest("Fred")

    def test_guest1_has_name(self):
        self.assertEqual("Abbie", self.guest1.name)

    # def test_guest_wrong_name_fails(self):
    #     self.assertEqual("Susan", self.guest1.name)

    def test_guest4_has_name(self):
        self.assertEqual("Dave", self.guest4.name)