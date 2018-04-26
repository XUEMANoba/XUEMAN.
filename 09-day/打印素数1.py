for i in range(2,100):
    a=1
    for j in range(int(i/2)):
        if (1+i)%(2+j)==0 :
            a=0
            break
    if a==1 :
        print(i+1)
