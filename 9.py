'''

find all permutations of a+b+c=1000



'''

sets = []
a = 1

for x in range(1,998):
	for y in range(1,998):
		if not x == y:
			z = 1000-x-y
			if x**2 + y**2 == z**2:
				print x,y,z
				break

'''
while a < 997:
	#split b and c into 1000-a
	b = a + 1
	while b < (997-a):
		c = 1000-a-b

		#if its a new set, check for pythag
		if not set([a,b,c]) in sets:

			#check if pythag trip
			if a**2 + b**2 == c**2:
				print a,b,c
				break
			else:
				print 'cheking: '+str(a)+' '+str(b)+' '+str(c)+' | '+str(len(sets))
				#try adding new set to sets
				sets.append(set([a,b,c]))
				b += 1
	a += 1
'''