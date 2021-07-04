def cofact(n, a, p, q):
    if n==1:
        return a
    else:
        rd=[]
        k=0
        for i in range(n):
            if i!=p:
                rd.append([])
            else:
                continue
            for j in range(n):
                if i!=p and j!=q:
                    rd[k].append(a[i][j])
            k+=1        
        return rd


def det(n, a):
    if n==1:
        return a[0][0]
    else:
        ans=0
        i=0
        for j in range(n):
            cofa=cofact(n, a, i, j)
            ans+= ((-1)**(i+j))*a[i][j]*det(n-1,cofa)
        return ans

def cofactor_mat(n, a):
    if n==1:
        return a
    else:
        emp=[]
        for i in range(n):
            emp.append([])
            for j in range(n):
                tmp= cofact(n, a, i, j)
                tp = ((-1)**(i+j))*det(n-1, tmp)
                emp[i].append(tp)
        return emp

def adj(n, a):
    if n==1:
        return a
    else: 
        rag=cofactor_mat(n,a)
        for i in range(n):
            for j in range(i,n):
                if i==j:
                    continue
                else:
                    rag[i][j]+= rag[j][i]
                    rag[j][i] = rag[i][j]-rag[j][i]
                    rag[i][j]-= rag[j][i]
        return rag

a=[]
b=[]
c=[]
n=int(input("Enter the number of variables\n"))
print("Convert all equations to a1.x1 + b1.x2+...=k1 form\nwhere a1, b1,...,k1 are constants and x1, x2... are unknowns\nNow Enter the constants in form of two matrices")
print("For ex:\n2x1 + 3x2 = 6\n4x1 + 7x2 = 9\nInput format is 2 matrices, 1 with coefficents of unknowns with space and another with constants of each eq separated with new line\n2 3\n4 7\n6\n9")
print("Now enter the two matrices of all your equations as shown in above format\n")
for i in range(n):
    a.append([])
    a[i]=list(map(int,input().split(" ")))
for i in range(n):
    b.append([])
    b[i].append(int(input()))
adj_a = adj(n, a)
for i in range(n):
    c.append([])
    tmp=0
    for j in range(n):
        k=0
        tmp+= adj_a[i][j]*b[j][k]
    c[i].append(tmp)
deter = det(n,a)
for i in range(n):
    j=0
    c[i][j]= c[i][j]/deter
if n==1:
    print("x1 = ",c[i][0]/deter, sep='')
else:
    for i in range(n):
        print("x",(i+1)," = ",c[i][0], sep='')
was=input("Press enter to terminate")


    



        


