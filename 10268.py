while True :
	a = int(input())		
	data = []
	data = input().split()	
	data = list(map(int,data))
	temp = len(data)-1
	result = 0 
	for i in range(0,len(data)):
		result += (data[i]*temp)*(a**(temp-1))
		temp-=1
	print(int(result))
	