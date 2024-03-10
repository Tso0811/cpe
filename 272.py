data = []
key = 0
while True:
	try :
		data = input()
	
		for i in data :
			if i == '"' and key == 0:
				print("``",end = "")
				key = 1
			elif i =='"' and key == 1:
				print("''",end = "")
				key = 0
			else :
				print(i,end = "")
		print("")
	except EOFError:
		break