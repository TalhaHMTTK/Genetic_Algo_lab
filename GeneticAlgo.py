import random

def Genetic_algo(arr1,arr2,n):
    temp=[]
    for i in range(n):
        temp.append(0)
    r=random.randint(1,n)
    for i in range(r):
        temp[i]=arr1[i]
    for i in range(r):
        arr1[i]=arr2[i]
        arr2[i]=temp[i]

    r1=random.randint(1,n-1)
    val1=random.randint(1,n-1)
    r2=random.randint(1,n-1)
    val2=random.randint(1,n-1)
    arr1[r1]=val1
    arr2[r2]=val2
    return
def copy_max(arr,max,n):
    for i in range(n):
        max[i]=arr[i]
    return

def aq(pos_arr,n):
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            if pos_arr[i]-i == pos_arr[j]-j:
                sum += 1
            elif pos_arr[i] == pos_arr[j]:
                sum += 1
            elif pos_arr[i] + i == pos_arr[j] + j:
                sum += 1

    return sum


def fit_fun(arr,n,pos_arr):
    total_fit=0

    for f in range(n):
        total_fit += f
    #print(total_fit)
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                pos_arr[j] = i
    x = aq(pos_arr,n)


    total_fit -= x
    return total_fit

def fit_fun2(n,pos_arr):
    total_fit=0

    for f in range(n):
        total_fit += f
    x = aq(pos_arr,n)
    total_fit -= x

    return total_fit

def create2DArray(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def EnterQueens(arr,n):
    for i in range(n):
        r=random.randint(0,n-1)
        arr[r][i]=1
    return arr


n=5



arr1=create2DArray(n)
arr2=create2DArray(n)
arr3=create2DArray(n)
arr4=create2DArray(n)

arr1=EnterQueens(arr1,n)
arr2=EnterQueens(arr2,n)
arr3=EnterQueens(arr3,n)
arr4=EnterQueens(arr4,n)

print(arr1)
print(arr2)
print(arr3)
print(arr4)

pos_arr1 = []
pos_arr2=[]
pos_arr3=[]
pos_arr4=[]
for _ in range(n):
    pos_arr1.append(0)
    pos_arr2.append(0)
    pos_arr3.append(0)
    pos_arr4.append(0)

maxi=0
max_pos_arr=[]
for _ in range(n):
    max_pos_arr.append(0)
a=fit_fun(arr1,n,pos_arr1)
copy_max(pos_arr1,max_pos_arr,n)
maxi=a
b=fit_fun(arr2,n,pos_arr2)
if b > maxi:
    copy_max(pos_arr2, max_pos_arr, n)
    maxi=b
c=fit_fun(arr3,n,pos_arr3)
if c > maxi:
    copy_max(pos_arr3, max_pos_arr, n)
    maxi=c
d=fit_fun(arr4,n,pos_arr4)
if d > maxi:
    copy_max(pos_arr3, max_pos_arr, n)
    maxi=d

print(pos_arr1)
print(pos_arr2)
print(pos_arr3)
print(pos_arr4)
#Genetic_algo(pos_arr1,pos_arr2,n)
#Genetic_algo(pos_arr3,pos_arr4,n)

for i in range(50):
    Genetic_algo(pos_arr1, pos_arr2, n)
    Genetic_algo(pos_arr3, pos_arr4, n)
    a = fit_fun2(n, pos_arr1)

    if a > maxi:
        copy_max(pos_arr1, max_pos_arr, n)
        maxi = a
    b = fit_fun2(n, pos_arr2)
    if b > maxi:
        copy_max(pos_arr2, max_pos_arr, n)
        maxi = b
    c = fit_fun2(n, pos_arr3)
    if c > maxi:
        copy_max(pos_arr3, max_pos_arr, n)
        maxi = c
    d = fit_fun2(n, pos_arr4)
    if d > maxi:
        copy_max(pos_arr3, max_pos_arr, n)
        maxi = d



print("maximun fitness of Queens Placement found at ",max_pos_arr)

