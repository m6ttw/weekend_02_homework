import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Mr. Brightside", "The Killers", "Rock")
        self.song2 = Song("Juicy", "The Notorious B.I.G.", "Rap")
        self.song3 = Song("Dancing Queen", "ABBA", "Pop")
        self.song4 = Song("Ring of Fire", "Johnny Cash", "Country")
        self.song5 = Song("No Scrubs", "TLC", "R&B")
        self.song6 = Song("Fly Me to the Moon", "Frank Sinatra", "Jazz")
        # self.song7 = Song()
        # self.song8 = Song()
        # self.song9 = Song()

    def test_song_has_title(self):
        self.assertEqual("Juicy", self.song2.title)

    def test_song_has_artist(self):
        self.assertEqual("TLC", self.song5.artist)