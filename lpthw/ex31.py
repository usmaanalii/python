print "You can enter a dark room with two doors. Do you go through door #1 or door #2 \
or door #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear"
	
	bear = raw_input("> ")
	
	if bear == "1": # nested if statements
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away" % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina"
	print "1. Blueberries"
	print "2. Yellow jacket clothespins"
	print "3. Understanding revolvers yelling melodies"
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of much, Good job!"

elif door == "3":
	print "You see a few items, which one do you select?"
	print "1. Knife"
	print "2. Spoon"
	print "3. Gun"
	
	selection = raw_input("> ")
	
	if selection == "3":
		print "You killed the bear, you are a G"
	else:
		print "Why didn't you pick the gun, you mong?"

else:
	print "You stumbe around and fall on a knife and die. Good job"
