import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("CC Caraoke Bar", [], [])

    def test_room_has_name(self):
        self.assertEqual("CC Caraoke Bar", self.room.name)

    def test_room_has_guest(self):
        self.assertEqual("Abbie", self.room.guests[0])