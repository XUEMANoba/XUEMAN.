'''
a = 0
b = 0

while a <= 100:
	print(a)	
	b+=a
	a+=2
print(b)
'''

i = 1
d_sum = 0#定义偶数和
s_sum = 0#定义技术和
while i <= 100:
	
	if i%2== 0:#偶数
		d_sum += i#加起来一定是偶数
	else:#奇数
		s_sum += i#加起来一定是奇数
	i+=1
print("偶数和%d"%d_sum)
print("奇数和%d"%s_sum)
