
temp = 0
case = int(input())
while True:
	temp+=1
	start_num = int(input())
	finish_num = int(input())
	sum = 0
	for i in range(start_num,finish_num+1):
		if i%2==0:
			continue
		sum+=i

	print("Case %d: %d"%(temp,sum))
	

