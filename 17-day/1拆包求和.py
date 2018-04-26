def sum(a,b,*args,**kwargs):
	sum1 = 0
	c = a+b
	sum1 += c
	for i in args:
		sum1+=i
	for i in kwargs.values():
		sum1+=i
	print(sum1)

t = (1,2)
b = {"age":12}
sum(1,2,*t,**b)
