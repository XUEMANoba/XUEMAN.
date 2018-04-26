list = []
def hanshu():
	i = 0
	all_sum = 0
	while i<=5:
		card = []
		score1 = int(input("请输入科目一分数"))
		score2 = int(input("请输入科目二分数"))
		score3 = int(input("请输入科目三分数"))
		card.append(score1)
		card.append(score2)
		card.append(score3)
		list.append(card)
		i+=1
		sum1 = score1+score2+score3
		all_sum +=sum1
		card1  = []
		card1.append(sum1)
		n = max(card1)
		print("总分最高分是%d"%n)
		print("科目一分数为%d科目二分数为%d科目三分数为%d"%(score1,score2,score3))
hanshu()
