	
def cycle_length (i):
	count = 1
	while (i != 1):
		if i % 2 == 0 :
			i = i//2
			count+=1
		elif i % 2 != 0:
			i = i*3+1
			count+=1
	return count

while True :
	a , b = input().split()
	a , b = int(a),int(b)
	max_length = 0
	for i in range(min(a,b),max(a,b)+1):
		count = cycle_length(i)
		if count > max_length :
			max_length = count
	print(a,b,max_length)
		