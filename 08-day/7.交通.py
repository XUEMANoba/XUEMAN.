juli = 7
money = 0
sum = 0
i = 1
while i<= 60:
	if juli <= 6:
		money = 3
	elif juli >6 and juli <=12:
		money = 4
	elif juli >12 and juli <=22:
		money = 5
	elif juli >22 and juli <=32:
		money = 6
	elif juli >32:
		if (juli - 32)%20 == 0:
			money = 6+(juli-32)/20
		else:
			money = 6+int(juli -32)/20+1
		
	if sum >= 100 and sum < 150:
		money = money*0.8
	elif sum>=150 and sum <400:
		money = money*0.5

	sum = sum + money

	i+=1
print("钱是%.02f"%sum)



