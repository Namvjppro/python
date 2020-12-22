def solution(N):
	dem =0
	x=0
	while N!=0 :
		if N%2==1 :
			N=N//2
			while N!=0 :
				if N%2==0 :
					dem+=1
					if x<dem :
						x=dem
					N=N//2
				else :
					dem=0
					N=N//2
			
		else: 
			N=N//2 
	if x!=0:
		return x
	else :
		return 0
N=int(input('nhap N:'))
print(solution(N))
	


