print("学生成绩管理系统".center(30,"*"))
print("1.录入成绩".center(30," "))
print("2.修改成绩".center(30," "))
print("3.查询成绩".center(30," "))
print("4.打印菜单".center(30," "))
print("5.删除成绩".center(30," "))
print("6.退出系统".center(30," "))
cards = []
while True:
	fun_num = int(input("请选择功能:"))
	if fun_num ==1:
		print("录入成绩")
		card={}#定义空字典
		flag = 0
		student_id = int(input("请输入学号:"))
		for temp in cards:
			if student_id == temp["student_id"]:
				flag = 1
				break
		if flag == 1:
			print("此学号已存在")
			continue
		name = input("请输入名字:")

		subject1 = input("请输入科目1:")
		subject2 = input("请输入科目2:")
		subject3 = input("请输入科目3:")
		score1 = int(input("请输入科目1分数:"))
		score2 = int(input("请输入科目2分数:"))
		score3 = int(input("请输入科目3分数:"))

		card["student_id"] = student_id
		card["name"] = name
		card["subject1"] = subject1
		card["subject2"] = subject2
		card["subject3"] = subject3
		card["score1"] = score1
		card["score2"] = score2
		card["score3"] = score3
		cards.append(card)
		print("录入成功")

	elif fun_num ==2:
		print("修改成绩")
		student_id = int(input("请输入要修改的学号:"))
		for temp in cards:
			if student_id == temp["student_id"]:
				print("1.修改科目1".center(30," "))
				print("2.修改科目2".center(30," "))
				print("3.修改科目3".center(30," "))
				print("4.修改科目1分数".center(30," "))
				print("5.修改科目2分数".center(30," "))
				print("6.修改科目3分数".center(30," "))
				change = int(input("请输入要修改的序号:"))
				if change == 1:
					subject1 = input("请输入新的科目1:")
					temp["subject1"] = subject1
				elif change == 2:
					subject2 = input("请输入新的科目2:")
					temp["subject2"] = subject2
				elif change == 3:
					subject3 = input("请输入新的科目3:")
					temp["subject3"] = subject3
				elif change == 4:
					score1 = int(input("请输入新的科目1分数:"))
					temp["score1"] = score1
				elif change == 5:
					score2 = int(input("请输入新的科目2分数:"))
					temp["score2"] = score2
				elif change == 6:
					score3 = int(input("请输入新的科目3分数:"))
				else:
					print("输入有误")
	elif fun_num ==3:
		student_id = int(input("请输入要查询的学号:"))
		flag = 0
		for temp in cards:
			if student_id == temp["student_id"]:
				flag = 1
				print("学号:%d\n姓名:%s\n科目1:%s科目1分数:%d\n科目2:%s科目2分数:%d\n科目3:%s科目3分数:%d\n"%(temp["student_id"],temp["name"],temp["subject1"],temp["score1"],temp["subject2"],temp["score2"],temp["subject3"],temp["score3"]))
			elif flag ==0:
				print("查无此人")
	elif fun_num ==4:
		print("学号\t姓名\t科目1\t科目1成绩\t科目2\t科目2成绩\t科目3\t科目3成绩")
		for temp in cards:
			print("%-12d%-12s%-12s%-12s%-12s%-12s%-12s%-12s"%(temp["student_id"],temp["name"],temp["subject1"],temp["score1"],temp["subject2"],temp["score2"],temp["subject3"],temp["score3"]))
	elif fun_num ==5:
		student_id = int(input("请输入要删除的学号:"))
		flag = 0
		for temp in cards:
			if student_id ==temp["student_id"]:
				flag = 1
				delete = input("请输入要删除的科目1=科目1,2=科目2,3=科目3:")
				if delete ==1:
					queren = int(input("0确认删除1返回:"))
					if queren ==0:
						cards.pop(subject1)
						print("删除成功")
					else:
						continue
				elif delete ==2:
					queren = int(input("0确认删除1返回:"))
					if queren ==0:
						cards.pop(subject2)
						print("删除成功")
					else:
						continue
				elif delete ==3:
					queren = int(input("0确认删除1返回:"))
					if queren ==0:
						cards.pop(subject3)
						print("删除成功")
					else:
						continue
		if flag ==0:
			print("没有此人")
	else:
		exit = int(input("0确认退出1返回"))
		if exit ==0:
			print("退出成功")
			break
		else:
			continue

