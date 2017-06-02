from multiprocessing import Pool
from itertools import chain

def FrequentWords(start):

	if start % 10000 == 0:
		print start

	index = {}
	for i in range(start, start + l - k + 1):
		word = genome[i:(i+k)]
		count = index.get(word,  0) + 1
		index[word] = count

	return [word for (word, count) in index.items() if count >= t]


if __name__ == '__main__':

	k = 9
	l = 500
	t = 3

	with open('E_coli.txt', 'r') as myfile:
		genome=myfile.read()

	#genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
	#k = 5
	#l = 50
	#t = 4

	p = Pool() # use all available CPUs
	result = p.map(FrequentWords, range(0, len(genome) - l + 1))

	print ' '.join(set(chain(*result)))