def haha():
	list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
	for i in list:
		for e in i:
			for o in i[e]:
				print("%s%s:%s"%(e,o,i[e][o]))
haha()



