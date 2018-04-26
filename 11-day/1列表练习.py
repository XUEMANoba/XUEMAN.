games = [["传奇","贪玩蓝月"],["QQ飞车","QQ炫舞"],["天天酷跑","天天炫斗"],["王者荣耀","绝地求生"]]
for i in games:
	for e in i:
		print("我喜欢玩%s"%e)


i = 0
while i < len(games):#0,1,2,3
	#print(games[i])
	j = 0
	while j < len(games[i]) :
		print("while我喜欢%s"%games[i][j])
		j+=1
	i+=1
