# arr=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# arr.sort(key=lambda s:(s[1],s[0]))
# print(arr)
# print(5&4)
#
# 10
# 94 R
# 74 L
# 90 L
# 75 R
# 37 R
# 99 R
# 62 R
# 4 L
# 92 L
# 44 R

def func4():
    """美团面试中的机器人坐标轴上的爆炸问题"""
    nums=int(input().strip())
    leftvalues=[]
    rightvalues=[]
    explode={}
    res=[]
    resdict={}
    for i in range(nums):
        values=input().strip().split()
        if values[-1]=="R":
            rightvalues.append(int(values[0]))
        elif values[-1]=="L":
            leftvalues.append(int(values[0]))
        explode[int(values[0])] = False
        res.append(int(values[0]))
    leftvalues.sort()
    rightvalues.sort(reverse=True)
    for j in rightvalues:
        for i in leftvalues:
            if j<i and  explode[i]==False and (i-j)%2==0:
                explode[i]=True
                explode[j]=True
                resdict[i]=(i-j)//2
                resdict[j]=(i-j)//2
                break
        else:
            resdict[j] = -1
    for k in leftvalues:
        if explode[k]==False:
            resdict[k]=-1

    result=[]
    for i in res:
        result.append(resdict[i])
    print(result)


