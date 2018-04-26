
'''
for i in range(2,100):
	if (i%2 !=0 and i%3 !=0 and i%5 !=0 and i%7 !=0) or i==2 or i==3 or i==5 or i==7:
		print(i)
'''



for i in range(2,101):
	a = 0
	for j in range(2,i):
		if i%j ==0:
			a = 1
			break
	if a==0:
		print(i)

'''
 for i in range(2,100):
     a=1
     for j in range(int(i/2)):
         if (1+i)%(2+j)==0 :
             a=0
             break
     if a==1 :
         print(i+1)
'''
