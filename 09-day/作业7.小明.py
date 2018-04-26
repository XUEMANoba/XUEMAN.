print("  ****地铁乘车消费计算计算器****  ")
distance = input("请输入您乘车区间的距离，距离大于0：")       #输入您的乘车距离0.5
if distance ==0:
	print("您还是原地呆着吧")
	exit()
	cost = 0.0
	day = 1
#while day<=20:
while day <= 40:
	rate = 0.0
# i = 1
# while i<=2:
	if cost>=100 and cost<150:
		rate = 0.8
	elif cost>=150 and cost<400:
		rate = 0.5
	else:
		rate = 1.0
	if distance <=6:
  		cost += (3*rate)
	elif distance > 6 and distance <= 12:
  		cost += (4*rate)
	elif distance > 12 and distance <= 22:
  		cost += (5*rate)
	elif distance > 22 and distance <= 32:
  		cost += (6*rate)
	else:
		if (distance-32)%20 == 0:
   			cost += ((6+(distance-32)/20)*rate)
		else:
   			cost += ((6+(distance-32)/20+1)*rate)
	day += 1
print("您在地铁花费的为%.2f"%cost)
