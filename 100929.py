def mod (a):
	if a%11 == 0:
		return True
	else:
		return False

while True : 
	a = int(input())	
	if a == 0 :
		break
	
	if mod(a)==True:
		print("%d is a multiple of 11." %a)
	else:
		print("%d is not a multiple of 11." %a)
		