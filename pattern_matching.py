def PatternMatch(pattern, genome):
	positions = []
	patternLength = len(pattern)

	for i in range(0, len(genome) - patternLength + 1):
		subText = genome[i:(i+patternLength)]
		if (subText == pattern):
			positions.append(i)

	return positions

with open('Vibrio_cholerae.txt', 'r') as myfile:
    genome=myfile.read()

print ' '.join([str(i) for i in PatternMatch("CTTGATCAT", genome)])