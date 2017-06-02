def FrequentWords(text, k):

	index = {}
	maxCount = 0

	for i in range(0, len(text) - k + 1):
		word = text[i:(i+k)]
		count = index.get(word,  0) + 1
		index[word] = count
		if count > maxCount:
			maxCount = count

	return [word for (word, count) in index.items() if count == maxCount]

print ' '.join(FrequentWords("CGCTCACAAGTCAGTCTCGCTTGGATCGTCAGTCTGTTATCTGAGTTATCTGACGCTTAGAGTCAGTCTCGCTTGGATCGTCAGTCTCGCTTAGACGCTTGGATCGTCAGTCTCGCTCACAACGCTTGGATCCGCTTGGATCCGCTCACAACGCTTGGATCGTTATCTGACGCTTAGAGTCAGTCTCGCTTAGACGCTTGGATCGTTATCTGAGTCAGTCTCGCTCACAAGTCAGTCTCGCTTGGATCCGCTTAGAGTTATCTGAGTTATCTGACGCTTGGATCCGCTTAGACGCTCACAAGTCAGTCTGTCAGTCTCGCTTGGATCGTCAGTCTGTTATCTGAGTCAGTCTCGCTTGGATCGTCAGTCTCGCTTAGACGCTCACAACGCTCACAACGCTTGGATCCGCTTAGAGTTATCTGACGCTCACAACGCTTGGATCGTCAGTCTCGCTTGGATCCGCTCACAACGCTTAGACGCTTGGATCGTCAGTCTGTCAGTCTCGCTTAGAGTCAGTCTCGCTTAGACGCTCACAACGCTTGGATCCGCTCACAAGTCAGTCTCGCTTGGATCGTTATCTGACGCTCACAAGTCAGTCTCGCTCACAACGCTCACAACGCTTAGAGTTATCTGAGTCAGTCTGTTATCTGAGTCAGTCTGTCAGTCTCGCTCACAAGTCAGTCTGTCAGTCTCGCTTAGAGTTATCTGAGTCAGTCTGTTATCTGACGCTTGGATCCGCTTAGACGCTCACAAGTCAGTCTCGCTCACAACGCTCACAACGCTTAGAGTCAGTCTCGCTCACAACGCTTAGACGCTTAGACGCTTAGAGTTATCTGACGCTTGGATCCGCTCACAACGCTCACAACGCTTAGACGCTTGGATCCGCTTAGACGCTCACAA", 11))