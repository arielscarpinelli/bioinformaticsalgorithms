def HammingDistance(p, q):

	distance = 0

	for i in range(0, len(p)):

		if p[i] != q[i]:
			distance = distance + 1

	return distance


def ApproximatePatternMatch(pattern, genome, distance):
	positions = []
	patternLength = len(pattern)

	for i in range(0, len(genome) - patternLength + 1):
		subText = genome[i:(i+patternLength)]
		if HammingDistance(subText, pattern) <= distance:
			positions.append(i)

	return positions

genome = "AACAAGCTGATAAACATTTAAAGAG"

result = ApproximatePatternMatch("AAAAA", genome, 2)

print ' '.join([str(i) for i in result])
print len(result)