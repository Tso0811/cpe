case = int(input())
e_count = 0
s_count = 0
while case!=0:

	a=[]
	a=input().split()
	for i in a :
		if i == "England":
			e_count+=1
		elif i == "Spain":
			s_count+=1
	case -= 1
print("England %d" %e_count)
print("Spain %d" %s_count)		