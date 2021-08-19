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
