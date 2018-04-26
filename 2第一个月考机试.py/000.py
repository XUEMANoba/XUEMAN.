def chengji():
	list = []
	list2 = []
	for i in range(5):
		list3 = []
		dict = {}
		while True:
			name = input('输入名字:')
			flag = 0
			for j in list:
				if name == j['name']:
					flag = 1
					print('名字重复,重新输入')
			if flag == 0:
				break
		yuwen = float(input('输入语文成绩:'))
		shuxue = float(input('输入数学成绩:'))
		yingyu = float(input('输入英语成绩:'))
		list3.append(yuwen)
		list3.append(shuxue)
		list3.append(yingyu)
		a = sum(list3)
		b = a/3
		dict['name'] = name
		dict['yuwen'] = yuwen
		dict['shuxue'] = shuxue
		dict['yingyu'] = yingyu
		dict['sum'] = a
		dict['average'] = b
		list2.append(a)
		list.append(dict)
	max_nu = max(list2)
	for i in list:
		if max_nu == i['sum']:
			print('*'*10)
			print('姓名:%s\n语文成绩:%0.2f\n数学成绩:%0.2f\n英语成绩:%0.2f\n平均成绩:%0.2f\n总分:%0.2f'%(i['name'],i['yuwen'],i['shuxue'],i['yingyu'],i['average'],i['sum']))
			print('*'*10)
chengji()
