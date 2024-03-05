case = int(input())
while (case != 0) :
	num = []
	a = input().split()
	num.extend(a)
	num = list(map(int,num)) #將list轉為int
	length = num.pop(0)
	min = 3000000000000000000000 
	result = 0
	for i in range(0,length) :
		for j in range(0,length):
			result += abs(num[i]-num[j])
		if result < min :
			min = result
		result = 0
	print(min)
	case = case-1
		
		 
		
	
	
	
	
	
	