high = float(input("请输入你的身高(m):"))
weidth = float(input("请输入你的体重(kg):"))
BMI= weidth/high**2

if BMI < 18.5:
	print("太轻了")
elif BMI>=18.5 and BMI<=25:
	print("正常")
elif BMI>=25 and BMI<=28:
	print("过重")
elif BMI>=38 and BMI<=32:
	print("肥胖")
elif BMI > 32:
	print("严重肥胖")
