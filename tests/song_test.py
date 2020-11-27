import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Mr. Brightside", "The Killers", "Rock")

    def test_song_has_title(self):
        self.assertEqual("Mr. Brightside", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("The Killers", self.song_1.artist)

    def test_song_has_genre(self):
        self.assertEqual("Rock", self.song_1.genre)