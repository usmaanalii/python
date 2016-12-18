from random import randint

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
	def remix(self):
		for line in self.lyrics:
			remix_words = ['What', 'You', 'Sayin', 'My', 'G']
			words = line.split()
			words[randint(0, len(words) - 1)] = remix_words[randint(0, len(remix_words) - 1)]
			print ' '.join(words)
			

happy_bday = Song(["Happy birthday to you", 
					"I dont want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of snails"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Study Drills
print '-' * 10
random = Song(["Is it too late now to say...",
				"I know I know I know I know I know", 
				"You light, the stars, up above me..."])

random.remix()
print '-' * 10
happy_bday.remix()
print '-' * 10
bulls_on_parade.remix()