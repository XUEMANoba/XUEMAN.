list = []
dict = {}
a = 0
while True:
	#输入
	name = input("请输入名字")
	age = int(input("请输入年龄"))
	sex = input("请输入性别")
	qq_id = int(input("请输入qq号码"))
	weight = float(input("请输入体重"))

	panduan = False
	for i in list:
		if i["姓名"] == name:
			panduan = True
			print("用户名存在")
			continue
	if not panduan:
		list.append({"姓名":name,"年龄":age,"性别":sex,"qq号":qq_id,"体重":weight})
	print(list)
	a+=1

age += age
average = age/a
print("平均年龄为%d"%average)
