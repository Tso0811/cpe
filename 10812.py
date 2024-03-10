case = int(input())
while case != 0 :
	s,d = input().split()
	s,d = int(s),int(d)


	score_b = (s-d)//2
	score_a = s-score_b 
	
	
	if score_a < 0 or score_b < 0:
		print("impossible")
	elif (s-d)%2 != 0:
		print("impossible")
	else:
		print("%d %d" %(max(score_b,score_a),min(score_a,score_b)))
	case-=1
