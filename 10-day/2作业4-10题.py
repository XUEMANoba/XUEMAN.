jiabin = ["诸葛亮","貂蝉","兰陵王"]
for i in jiabin:
	print("跟我一起吃饭吧"+i)

print("%s无法赴约"%jiabin[0])
jiabin[0] = "百里守约"
for a in jiabin:
	print("跟我一起吃饭吧"+a)

print("我找到了一个更大的餐桌")
jiabin.insert(0,"狄仁杰")
jiabin.insert(3,"赵云")
jiabin.append("白起")
for o in jiabin:
	print("跟我一起吃饭吧"+o)

print("因为餐桌不够只能邀请两位嘉宾了")
print(jiabin)

print(jiabin.pop(0)+"很抱歉桌子不够大我们下次再约吧")
print(jiabin.pop(1)+"很抱歉桌子不够大我们下次再约吧")
print(jiabin.pop(1)+"很抱歉桌子不够大我们下次再约吧")
print(jiabin.pop(1)+"很抱歉桌子不够大我们下次再约吧")
print(jiabin)
for e in jiabin:
	print("跟我一起吃饭吧"+e)
del jiabin[0]
del jiabin[0]
print(jiabin)


place = ["巴黎","丽江","大理","张家界","花果山"]
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)



print(len(place))



liebiao = ["电脑","手机","键盘","鼠标","耳机","水杯","奶茶"]
liebiao_2 = ["芒果","提子"]
liebiao.insert(0,"苹果")
print(liebiao)
liebiao.append("猕猴桃")
print(liebiao)
liebiao.extend(liebiao_2)
print(liebiao)
liebiao[0]="荔枝"
print(liebiao)
del liebiao[4]
print(liebiao)
#liebiao.remove["耳机"]
#print(liebiao)
liebiao.pop()
print(liebiao)
liebiao.pop(0)
print(liebiao)
print(len(liebiao))
print(liebiao.count("奶茶"))
liebiao.sort()
print(liebiao)
liebiao.sort(reverse=True)
print(liebiao)
liebiao.reverse()
print(liebiao)
print(liebiao.clear)

