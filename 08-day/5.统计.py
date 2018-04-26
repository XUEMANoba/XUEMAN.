num = 1
a = 0
while num <= 5000 and num >= 1:
	if num%5 == 0 or num%7 == 0:
		print("%d能被5和7整除"%num)
		a+=1
	num+=1
print("一共有%d个数能被5和7整除"%a)
