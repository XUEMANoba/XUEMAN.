number = 1
i = 0
while number<=5000 and number>=1:
	if number%5==0 and number%7==0:
		print("%d能被5和7整除"%number)
		i+=1
	number+=1
print("一共有%d个数能被5和7整除"%i)
