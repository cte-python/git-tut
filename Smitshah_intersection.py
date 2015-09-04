a=[12,36,5,2,7,9,3]
b=[3,4,5,6,7]
c=[]
i=0
while(i!=len(a)):
    j=0
    while(j!=len(b)):
        if(a[i]==b[j]):
            c.append(a[i])
        j=j+1
    i=i+1
print(c)


    