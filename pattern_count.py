def PatternCount(text, pattern):
	count = 0
	patternLength = len(pattern)

	for i in range(0, len(text) - patternLength + 1):
		subText = text[i:(i+patternLength)]
		if (subText == pattern):
			count = count + 1

	return count

print PatternCount("AAGAAGGCGAAAGGCGATAAGGCGAAAGGCGACACGATCGAAAGGCGACAAGGCGACAAGGCGAACTGCTAAAGGCGAGGTATTTAAGGCGAATCAAGGCGAATCAAGGCGAAAGGCGAATCAAGGCGAAAGGCGAACCTAAAGGCGACAAAGGCGAAAAAACACAAGGCGAGAAGGCGAAAGGCGACATCGACAAGGCGATCCTAAAGGCGATGATGAAGGCGAGTAAAGGCGATGAAGGCGAAAGGCGAAAAAGGCGATTAAAGGCGACCCAAGGCGAGGAAGGCGACAAAGGCGACAAGGCGAAAAAGGCGAGAAGGCGACCTAAGGCGATGAAGGCGAATGTCGACAAAGGCGAATAAGGCGACTTGGGCCAAAGGCGAAGGCAAAGGCGATAGTGAAGGCGAGTCACGGCAACCTCAAAGGCGAGCGTTTAAGGCGAAAGGCGAATTAAGGCGACGAGACAAAGGCGAGGCGATGAAGGCGAAAGGCGATGAAGGCGACAAGGCGAGCAAGGCGATAAGGCGATATTAAGGCGAGTTTAAGGCGAAAGGCGAGCGAAAGGCGATCAGGAAGGCGAAGTAAATTCACAAGGCGATACTAAGGCGAAAGGCGAGAAGGCGAAAGGCGAACAAAGGCGAAAGGCGAGAAGGCGAAAGGCGATGGCAAGGCGAAAGGCGAAAAGGCGAATAATAAGGCGAAATTAAGGCGAAAGGCGACTAAGGCGATAAGGCGAGCCCAAGGCGAAAGGCGAAAGGCGAGAAGGCGATGGTGTAAGGCGAAGGGAGCCAAGGCGAAAGAAGGCGATAGGTGATGAAGGCGAAAAGGCGAAAGGCGATAAGAAGGCGATATCCAAGGCGACAAGGCGAAAAGGCGAAAGGCGAGGTTTGTCAAGGCGAGTGGAAAGGCGATAAGGCGACAAAGGCGAAAGT", "AAGGCGAAA")