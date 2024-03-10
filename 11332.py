def main(i):
	sum = 0
	while i != 0 :
		sum = sum + (i%10)
		i//=10
	return sum

while True :
	a = int(input())
	if a == 0:
		break 
	
	while a >= 10 :
		a = main(a)
	print(a)
	
		
	