def stutter(word):
	stutter = word[0:2]		
	return stutter + '... ' + stutter + '... ' +  word + '?'
print(stutter('hola'))