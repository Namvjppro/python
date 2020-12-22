def he10to2(he10):
	if he10>0:
		x=he10%2
		he10to2(he10//2)
		print(x,end="")
dem =0
x=0
he10=int(input('nhap vao 1 so nguyen bat ky:'))
print('so',he10,'chuyen sang nhi phan se la:',end="")
he10to2(he10)
print("\n",'khoang cach nhi phan lon nhat cua',he10,'la:',end='')
while he10!=0 :
	if he10%2==1 :
		he10=he10//2
		while he10!=0 :
			if he10%2==0 :
				dem+=1
				if x<dem :
					x=dem
				he10=he10//2
			else :
				dem=0
				he10=he10//2
			
	else: 
		he10=he10//2 
print(x)
	


