import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Abbie")

    def test_guest1_has_name(self):
        self.assertEqual("Abbie", self.guest_1.name)