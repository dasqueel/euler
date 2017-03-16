'''

has to end in 0 or 5 for multiple of 5

has to be even due to divisable by 2

start at 2520 and keep adding 20 and do the test

'''

'''
#ineffcient first try at problem
def divByAll20(x):
	divList = [3,7,11,13,17,19]
	i = 0
	while (i < len(divList)):
		if x % divList[i] != 0:
			return divList[i]
		i += 1
	return 'found'

j = 1346881920

while True:
	if divByAll20 != 'found':
		print str(j)+'  -  '+str(divByAll20(j))
		j += 20
	else:
		print j
		break'''


#somewhat solution to solve the problem
def checker(x):
	divList = [18,17,16,15,14,13,12,11]
	i = 0
	while (i < len(divList)):
		if x % divList[i] != 0:
			return divList[i]
		i += 1
	return 'found'


print checker(232792560)

#j is the iteration count of 20
j = 10

found = False
while found == False:
	cur = 380 * j

	if checker(cur) != 'found':
		print str(j)+' - '+str(cur)+'  -  '+str(checker(cur))
		j += 1
	elif checker(cur) == 'found':
		print 'answer is: '+str(cur)
		found = True