def hawaiian_scrabble_score(str):
	alphabet = {'A':1, 'K':2, 'O':2, 'I':3, 'N':3, 'E':4, 'U':5, 'H':6, 'L':7, 'M':8, 'P':8, 'W':9}
	return sum([alphabet[c] if c in alphabet else -abajillion for c in str.upper()])

print hawaiian_scrabble_score('aloha')