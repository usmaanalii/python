def scan(sentence):
	words = sentence.lower().split()
	
	directions = ['north', 'east', 'south', 'west']
	verbs = ['go', 'stop', 'kill', 'eat']
	stops = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']

	pairs = []

	for word in words:
		if word in directions:
			pairs.append(('direction', word))
		elif word in verbs:
			pairs.append(('verb', word))
		elif word in stops:
			pairs.append(('stop', word))
		elif word in nouns:
			pairs.append(('noun', word))
		else:
			pairs.append(('error', word))

	return pairs
