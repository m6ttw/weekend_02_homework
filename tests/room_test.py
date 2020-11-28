import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Abbie")
        self.guest_2 = Guest("Bob")
        self.room_1 = Room("Opium")
        self.room_2 = Room("Hive")
        self.song_list_1 = [
            Song("Mr. Brightside", "The Killers", "Rock"),
            Song("Juicy", "The Notorious B.I.G.", "Rap"),
            Song("Dancing Queen", "ABBA", "Pop"),
            Song("Ring of Fire", "Johnny Cash", "Country"),
            Song("No Scrubs", "TLC", "R&B"),
            Song("Fly Me to the Moon", "Frank Sinatra", "Jazz"),
            Song("Anarchy in the U.K.", "Sex Pistols", "Punk"),
            Song("No Woman, No Cry", "Bob Marley and the Wailers", "Reggae"),
            Song("Wake Me Up", "Avicii", "Dance")
            ]

    def test_room_has_name(self):
        self.assertEqual("Opium", self.room_1.name)

    def test_can_add_song_to_room(self):
        self.room_1.add_song(self.song_list_1[0])
        self.assertEqual(1, self.room_1.song_count())

    def test_can_add_guest_to_room(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())