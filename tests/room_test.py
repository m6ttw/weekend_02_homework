import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Mr. Brightside", "The Killers", "Rock")
        self.song2 = Song("Juicy", "The Notorious B.I.G.", "Rap")
        self.song3 = Song("Dancing Queen", "ABBA", "Pop")
        self.song4 = Song("Ring of Fire", "Johnny Cash", "Country")
        self.song5 = Song("No Scrubs", "TLC", "R&B")
        self.song6 = Song("Fly Me to the Moon", "Frank Sinatra", "Jazz")
        self.song7 = Song("Anarchy in the U.K.", "Sex Pistols", "Punk")
        self.song8 = Song("No Woman, No Cry", "Bob Marley and the Wailers", "Reggae")
        self.song9 = Song("Wake Me Up", "Avicii", "Dance")
        self.room = Room("CC Caraoke Bar")
        self.guest1 = Guest("Abbie")
        self.guest2 = Guest("Bob")
        self.guest3 = Guest("Carol")
        self.guest4 = Guest("Dave")
        self.guest5 = Guest("Emma")
        self.guest6 = Guest("Fred")

    def test_room_has_name(self):
        self.assertEqual("CC Caraoke Bar", self.room.name)

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song1)
        self.assertEqual(1, self.room.song_count())

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest1)
        self.assertEqual(1, self.room.guest_count())