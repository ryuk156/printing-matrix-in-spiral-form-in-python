x=[[1,2,3,11],
   [8,9,4,12],
   [7,6,5,13],
    ]




k=0
l=0
m=3
n=4


while(k<m and l<n):
    for i in range(l,n):
        print(x[k][i])

    k=k+1

    for i in range(k,m):
        print(x[i][n-1])

    n=n-1
    if(k<m):
        for i in range(n-1,l-1,-1):
            print(x[m-1][i])
        m=m-1

    if(l<n):
        for i in range(m-1,k-1,-1):
            print(x[i][l])
        l+=1







####first row11
##for i in range(l,n):
##    print(x[k][i])
##
##
####now go in second row by increamenting m by 1     
##k=1
##for i in range(l,m):
##    print(x[i][n-1])
##
##
##n=n-1
##
##for i in range(n-1,l-1,-1):
##    
##    print(x[m-1][i])
##m=m-1
##for i in range(m-1,k-1,-1):
##    print(x[i][l])
##
##l+=1



