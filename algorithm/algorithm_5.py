import itertools
import copy
#  导入具体的类型限制
import math
from typing import List


def islegal(ip):
    n=len(ip)
    res=[]
    # 这个地方直接使用组合的方式进行判断
    pos=itertools.combinations([i for i in range(1,n)],3)
    for i in pos:
        if i is not None:
            if checkip([ip[:i[0]],ip[i[0]:i[1]],ip[i[1]:i[2]],ip[i[2]:]]):
                res.append(".".join([ip[:i[0]],ip[i[0]:i[1]],ip[i[1]:i[2]],ip[i[2]:]]))
    return res


def checkip(iplist):
    """检查一个ip 是否合法"""
    for segment in  iplist:
        if len(segment)>1 and segment[0]=="0":
            return False
        try:
            if int(segment)>255:
                return False
        except:
            return False

    return True




def func1():
    """ 使用官方API 实现重复排序"""
    from itertools import product
    a=[2,3,4,5,6]
    b=list(product(a,repeat=len(a)))
    print(b)

def func2():
    """ 使用官方API 实现不重复排序"""
    from itertools import permutations
    #  默认每一个都是不同的元素
    a = [2 ,3, 4, 5, 6]
    b = list(permutations(a))
    print(b)


def func3():
    from itertools import combinations
    a = [2 ,3, 4, 5]
    #从a 中选出三个元素
    b = list(combinations(a,3))
    print("=======",b)



def repeatpermutationss():
    """ 包含重复元素的排列"""
    res=[]
    import copy
    def dfs(a,temp):
        if len(temp)==len(a):
            res.append(copy.deepcopy(temp))
            return
        for i in a:
            temp.append(i)
            dfs(a,temp)
            temp.pop()

    dfs([2,3,4,5,6],[])
    return res


def permutations(arr, position, end):
    """不包含重复元素的排列， 使用递归进行排列"""
    if position == end:
        res.append(copy.deepcopy(arr))
        # print(arr)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]



def permutationss():
    """使用回溯进行排序，　需要使用visit 来判断一个位置是否被遍历过了 """
    res=[]
    import copy
    def dfs(a,temp,visit):
        if len(temp)==len(a):
            res.append(copy.deepcopy(temp))
            return
        for i in range(len(v)):
            if visit[i]==False:
                visit[i]=True
                temp.append(v[i])
                dfs(v,temp,visit)
                temp.pop()
                visit[i]=False
    v=[2,2,4,5,6]
    visit=[False for _ in range(len(v))]
    dfs(v,[],visit)
    return res



res=[]
arr = [3,6,7,1]
permutations(arr, 0, len(arr))
print(res)
# func2()
# print(permutationss())
# func3()

import copy

def combine(l, n):
    answers = []
    one = [0] * n
    def next_c(li = 0, ni = 0):
        if ni == n:
            answers.append(copy.copy(one))
            return
        #这个地方是什么原理
        for lj in range(li, len(l)):
            one[ni] = l[lj]
            next_c(lj + 1, ni + 1)
    next_c()
    return answers

# print(combine([1, 2,2, 3, 4, 5], 3))



def combines():
    a=[1, 2, 3, 4, 5]
    n=3
    answers = []
    one = [0] * n
    def dfs(l,templen):
        if templen==n:
            answers.append(copy.copy(one))
            return
            # 两个位置都做了限制操作,后边的位置然后通过l 来进行限制操作
        for i in range(l,len(a)):
            one[templen]=a[i]
            dfs(i+1,templen + 1)

    dfs(0,0)
    print("=============")
    print(answers)

# combines()


def subset():
    """几天不写这个代码就这么拉了哈哈，求一个序列的子集都求了半天"""
    a=[1, 2, 3]
    res=[[]]
    for item in a:
        for i in range(len(res)):
            # i.append() 不会返回任何东西可以操作,python 中也是需要deepcopy 的操作， 别以为这个不需要
            temp=copy.deepcopy(res[i])
            temp.append(item)
            res.append(temp)
    print(res)
# subset()

"""
  while s[start]!="[" and s[start].isdecimal()==False:
            start+=1
        res+=s[:start]
        for i in range(start,len(s)):
            if s[i]=="[":
                stack.append(i)
            if s[i]=="]":
                st=stack.pop()
                temp=st-1
                while temp>=0 and s[temp].isdecimal():
                    temp-=1
                if temp==st-1:
                    times=1
                else:
                    print(temp,st)
                    times=int(s[temp+1:st])
                res=s[st+1:i]*times+res
"""

# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack=[]
#         for i in  s:
#             if i!="]":
#                 stack.append(i)
#             else:
#                 substring=""
#                 while  stack[-1].isalpha():
#                         substring=stack.pop()+substring
#                 stack.pop()
#                 times=""
#                 while len(stack)>0 and stack[-1].isdecimal():
#                     times=stack.pop()+times
#                 if len(times)==0:
#                     flod=1
#                 else:
#                     flod=int(times)
#
#                 # 之前的进行合并
#                 total=substring*flod
#                 while len(stack)>0 and stack[-1].isalpha():
#                     total=stack.pop()+total
#                 stack.append(total)
#         print(stack)
#         return "".join(stack)
#
# a=Solution()
# print("==========")
# print(a.decodeString("2[abc]3[cd]ef"))


class Solution:
    def __init__(self):
        self.res = 0

    def numDecoding(self, s):
        self.dfs(0, s)
        return self.res

    def dfs(self, k, s):
        if k == len(s):
            self.res += 1
            return
        for j in range(1, 3):
            if k + j > len(s):
                return
            elif len(s[k:k+j]) > 1 and s[k] == "0":
                return
            elif 0 < int(s[k:k + j]) <= 26:
                self.dfs(k+ j, s)

print("================")
c=Solution()
print(c.numDecoding("226"))






a="1223"
b="1"
# if b in a:
#     print(a.index(b))
# else:
#     print(-1)

def func4():
    index=-1
    for i in range(len(a)):
        if a[i]==b[0] and a[i+1:i+len(b)]==b[1:]:
            index=i
            break
    print(index)

def func5():
    """获取栈中的合法的括号的长度"""
    a=")("
    stack=[]
    for index,val in enumerate(a):
        if val==")":
            if len(stack)>0 and a[stack[-1]]=="(":
                stack.pop()
            else:
                stack.append(index)
        elif val=="(":
            stack.append(index)
    print(stack)
    print("=========",int())

class Solution:
    """ 网易面试判断路径的最短值,走到目的地址的最短的路径"""
    def minSailCost(self , inputs ):
        # write code here
        dptable=[[float("inf")]* len(inputs[0])for i in range(len(inputs))]
        # 初始化边界条件
        dptable[0][0]=0
        print(dptable)
        for i in range(1,len(inputs)):
            if inputs[i][0]==0:
               dptable[i][0]=dptable[i-1][0]+2
            elif inputs[i][0]==1:
               dptable[i][0]=dptable[i-1][0]+1
            else:
                break
        for i in range(1,len(inputs[0])):
            if inputs[0][i]==0:
               dptable[0][i]=dptable[0][i-1]+2
            elif inputs[0][i]==1:
               dptable[0][i]=dptable[0][i-1]+1
            else:
                break
        print(dptable)
        for i in range(1,len(inputs)):
            for j in range(1,len(inputs[0])):
                if inputs[i][j]==0:
                   dptable[i][j]=min(dptable[i-1][j],dptable[i][j-1])+2
                elif inputs[i][j]==1:
                   dptable[i][j]=min(dptable[i-1][j],dptable[i][j-1])+1
                else:
                    continue
        if dptable[len(inputs)-1][len(inputs[0])-1]==float("inf"):
            return -1
        return dptable[len(inputs)-1][len(inputs[0])-1]


h=Solution()
print(h.minSailCost([[1,1,1,1,0],[0,1,0,1,0],[1,1,2,1,1],[0,2,0,0,1]]))


def func6():
    """网易的面试题贪心算法判断最短的路径"""
    nums=[int(i) for i in input().strip().split()]
    res=0
    n=len(nums)
    res=[1 for _ in range(n)]
    for i in range(n):
        lindex=(i-1)%n
        rindex=(i+1)%n
        if nums[i]>nums[lindex]  and nums[i]>nums[rindex]:
            res[i]=max(res[lindex],res[rindex])+1
        elif nums[i]>nums[lindex]  and nums[i]<=nums[rindex]:
            res[i]=res[lindex]+1
        elif nums[i]>nums[rindex] and  nums[i]<=nums[lindex]:
            res[i]=res[rindex]+1
    print(sum(res))

def func7():
    """
    判断两个位置是否是邻居，
    就是两个位置是否是对角线上的元素
    :return:
    """
    n=int(input().strip())
    nums=[]
    for _ in range(n):
        nums.append([int(i) for i in input().split()])
    res=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i][0]== nums[j][0] or nums[i][1]== nums[j][1]:
                continue
            temp=(nums[j][1]-nums[i][1])/(nums[j][0]-nums[i][0])
            if temp==1 or temp==-1:
                res+=1
    print(res)

# 京东的竹子问题
def func4():
    """
    将一个竹子分割成可以的段进行操作， 只有三种分段可以， 然后问最多可以分多少段，采用完全背包的思路
    然后外层的循环是背包的元素， 内层的是背包容量的大小。
    :return:
    """
    nums=[int(i) for i in input().split()]
    n=nums[0]
    nums=nums[1:]
    minnum=min(nums)
    if n%minnum==0:
        print(n//minnum)
    else:
        left=n%minnum
        used=float("inf")
        for z in nums:
            if z!=minnum:
                temp=(z-left)/minnum
                if temp<used:
                    used=temp
        print(n//minnum-used+1)
        # 转换成完全背包的思路进行操作
        dp=[[0]*(n+1) for _ in range(4)]
        for i in range(1,4):
           for j in range(nums[i-1],n+1):
               dp[i][j]=max(dp[i][j-nums[i-1]]+1,dp[i-1][j])
        print(dp[3][n])


def visit(nums,used,target,count):
    """
    #  广度优先遍历操作，每次存储一个使用过的list然后进行遍历操作
    # 拼多多笔试题， 判断从一个数变到另一个数，所需用的最少的次数， 采用 广度优先遍历， 然后主要是进行剪枝操作，维护一个已经使用的列表
    :param nums:
    :param used:
    :param target:
    :param count:
    :return:
    """
    temp = []
    used.extend(nums)
    for i in nums:
        if i==target:
            return count
        else:
            for j in [i-1,i+1,i-2,i*2]:
                if j not in used and j not in temp:
                   temp.append(j)
    print(temp)
    return visit(temp,used,target,count+1)
print(visit([10],[],1,0))
# [9, 11, 8, 20]
# [7, 9, 6, 16, 8, 10, 7, 18, 10, 12, 9, 22, 19, 21, 18, 40]
# [5, 7, 4, 12, 6, 8, 5, 14, 7, 9, 6, 16, 8, 10, 7, 18, 9, 11, 8, 20, 39, 41, 38, 80, 11, 13, 10, 24, 15, 17, 14, 32, 17, 19, 16, 36, 18, 20, 17, 38, 20, 22, 19, 42, 21, 23, 20, 44]
# 判断数字需要 看最后的位数是否大于要求的位数
print(int(1000/730))
print(int(100/10))

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

