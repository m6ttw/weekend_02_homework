import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest_list = [
            Guest("Abbie"),
            Guest("Bob"),
            Guest("Carol"),
            Guest("Dave"),
            Guest("Emma"),
            Guest("Fred")
        ]

        self.room_1 = Room("Opium")
        self.room_2 = Room("Hive")

        self.song_list_1 = [
            Song("Mr. Brightside", "The Killers", "Rock"),
            Song("Back in Black", "AC/DC", "Rock"),
            Song("Walk", "Pantera", "Metal"),
            Song("Aerials", "System of a Down", "Metal"),
            Song("Welcome to the Jungle", "Guns N' Roses", "Rock")
        ]

        self.song_list_2 = [
            Song("Gold Digger", "Kanye West", "Hip hop"),
            Song("Shape of You", "Ed Sheeran", "Pop"),
            Song("Wannabe", "The Spice Girls", "Pop"),
            Song("I Write Sins Not Tragedies", "Panic! at the Disco", "Pop Punk"),
            Song("Wake Me Up", "Avicii", "Dance")
        ]

    def test_room_has_name(self):
        self.assertEqual("Opium", self.room_1.name)

    def test_can_add_guest_to_room(self):
        self.room_1.check_in_guest(self.guest_list[0])
        self.assertEqual(1, self.room_1.guest_count())

    def test_can_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_list_1[0])
        self.assertEqual(1, self.room_1.song_count())

