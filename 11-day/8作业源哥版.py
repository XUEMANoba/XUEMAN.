list = []
name_list = []
a = 0
while True:
	if a == 3:
		break
	#输入
	dict = {}
	name = input("请输入名字")
	age = int(input("请输入年龄"))
	sex = input("请输入性别")
	qq_id = int(input("请输入qq号码"))
	weight = float(input("请输入体重"))
	#字典赋值
	if name not in name_list:
		dict["name"] = name
		dict["age"] = age
		dict["sex"] = sex
		dict["qq_id"] = qq_id
		dict["weight"] = weight
		#添加字典到列表
		list.append(dict)
		name_list.append(dict["name"])#一定要记录
		print(list)
		a+=1
	else:
		print("名字重复")
age_sum = 0
#list = [{},{},{}]
for i in list:
	age_sum += i.get("age")
	print(i)
print("年龄的平均值为%0.2f"%(age_sum/len(list)))
