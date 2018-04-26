i = 1
sum = 0

while i < 100:

	if i%2 == 0:
		sum-=i
	else:
		sum+=i
	i+=1

print("1-2+3...的和为%d"%sum)
