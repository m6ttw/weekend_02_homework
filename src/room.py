
class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []



    def guest_count(self):
        return len(self.guests)
    
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def song_count(self):
        return len(self.songs)
    
    
    def add_song(self, song):
        self.songs.append(song)