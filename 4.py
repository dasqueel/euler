def isPali(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False


y = 999
biggest = 0
for x in range(836,999):
	for y in range(836,999):
		#print x,y,x*y
		if isPali(x*y):
			newBig = x*y
			if newBig > biggest:
				biggest = newBig
print biggest
'''
y = 999
biggest = 0
for x in range(836,999):
	while y >= 836:
		if isPali(y*x):
			print 'here'
			if y*x > biggest:
				biggest = y*x
		else:
			y = y - 1
			print y


print biggest

x = 999
y = 999


def find(x,y,biggest):
	if not isPali(x*y):
		find(x-1,y,biggest)
	else:
		newBig = x*y
		print x,y,x*y
		if newBig > biggest:
			return newBig
		else:
			return biggest

biggest = 0
while x > 836 and y > 836:

	biggest = find(x,y,biggest)
	break

print biggest
#find(999,999)

while not isPali(prod)

while True:

	i = 0
	while i < 50:
		#print y-i
		prod = x*(y-i)
		print prod
		if isPali(prod) == True:
			print prod
			break
		else:
			i = i + 1

def findLarge(x,y):
	i = 0
	while i <= 50:
		#print y-i
		prod = x*(y-i)
		#print prod
		if isPali(prod) == True:
			print prod
			break
		else:
			i = i + 1
'''