for num in range(1,201):
    dom = 0
    for fac in range(0,201):
        fac += 1
        if float(num)/float(fac) in range(1,201):
            dom += 1
    if dom == 2:
       print (num)
