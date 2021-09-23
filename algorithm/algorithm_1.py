# 读取第一行的n,找重复的位置
def func1():
    import  copy
    a = []
    b = []
    n = int(input().strip())
    for i in range(n):
        a.append(input().strip())
    m = int(input().strip())
    for i in range(m):
        b.append(input().strip())
    ans = 0
    if len(a) == 0:
        print(-1)
    else:
        temp = copy.deepcopy(a)
        for i in b:
            if i in temp:
                temp.remove(i)
                if len(temp) == 0:
                    ans += 1
                    temp = copy.deepcopy(a)
                    temp.remove(i)

        print(ans)

# 马走日的位置，使用回溯然后判断位置
def func2():
    x0, y0, x1, y1 = [int(i) for i in input().strip().split()]
    counter = 0

    def dfs(x0, y0, x1, y1):
        global counter
        if x0 == x1 and y0 == y1:
            counter += 1
        for step in [[2, 1], [1, 2]]:
            if x0 + step[0] <= x1 and y0 + step[1] <= y1:
                dfs(x0 + step[0], y0 + step[1], x1, y1)

    dfs(x0, y0, x1, y1)
    print(counter)
from threading import Thread
import queue
# queue1=queue.Queue()
# queue2=queue.Queue()
# queue3=queue.Queue()
# def orderprint(queueout,queuein):
#     for i in  range(5):
#         data=queueout.get()
#         print(chr(65+data))
#         newdata=(data+1)%3
#         queuein.put(newdata)
#
#
# t1=Thread(target=orderprint,args=(queue1,queue2,))
# t1.start()
# t1=Thread(target=orderprint,args=(queue2,queue3,))
# t1.start()
# t1=Thread(target=orderprint,args=(queue3,queue1,))
# t1.start()
# queue1.put(0)
# flag = g1
# temp = copy.deepcopy(records)
# for group in temp:
#     if group[0] == flag:
#         flag = group[1]
#         temp = copy.deepcopy(records)
#         temp.remove(group)
#         if flag == g2:
#             return 1
# flag = g2
# temp = copy.deepcopy(records)
# for group in temp:
#     if group[0] == flag:
#         flag = group[1]
#         temp = copy.deepcopy(records)
#         temp.remove(group)
#         if flag == g1:
#             return -1
# return 0

# -*- coding:utf-8 -*-
import copy
class Cmp:
    def cmp(self, g1, g2, records, n):
        # write code here
        self.flag=False
        self.dfs(g1, g2, records)
        if self.flag:
            return 1
        self.dfs(g2, g1, records)
        if self.flag:
            return -1
        return 0


    def dfs(self,g1, g2, records):
        if g1 == g2:
            self.flag = True
            return
        for group in records:
            if group[0] == g1:
                self.dfs(group[1], g2, records)




# a=Cmp()
# res=a.cmp(1,3,[[3,2],[2,4],[2,1],[4,1]],4)
# print(res)
# print(set([1,3,2])==set([12,3,3]))
#
# # def dfs(n):
# #     if n<=3:
# #         return n
# #     return dfs(n-1)+dfs(n-3)
# #
# #
# # print(dfs(6))
# print(set([12,4,12,4]))
# s="cbaebabacd"
# p="abc"
# if len(s) < len(p):
#     print([])
# res = []
# lp = list(p)
# lp.sort()
# windows = len(p)
# for i in range(len(s) - windows + 1):
#     temp = list(s[i:i + windows])
#     temp.sort()
#     if temp == lp:
#         res.append(i)
#         #
# print(res)
# #  直接使用集合进行去重操作
# a={2,3,3,4,5,5}
# print(a)
# nums=[1,2,3]
# res = [[]]
# import  copy
# for i in nums:
#     res=res+[one+[i] for one in res]
# print(res)
# print(7>>2)
# matrix=[[1,3]]
# target=3
# import numpy as np
# a = list(np.array(matrix).flatten())
# left, right = 0, len(matrix) - 1
# while left <= right:
#     mid = (left + right) // 2
#     if a[mid] == target:
#         print("good")
#     elif a[mid] > target:
#         right = mid - 1
#     else:
#         left = mid + 1
#
# dp=[[0,1] for i in range(5+1)]
# dp[0][0]=12
# print(dp)
# for i in range(1,5):
#     print(i)



class Solution:
    def max_version(self , version_list ):
        res=[]
        for version in version_list:
            first=[int(i) for i  in version[0].strip().split(".")]
            second=[int(i) for i  in version[1].strip().split(".")]

            if self.compare(first, second):
                res.append(1)
            else:
                res.append(2)
        return res
    def compare(self , version1 ,version2):
        n = len(version1) if len(version1) < len(version2) else len(version2)
        for i in range(n):
            if version1[i]>version2[i]:
                return True
            elif version1[i]==version2[i]:
                continue
            else:
                return False
            # 如果第二个的长度比第一个的长度长，就认为第二个的版本高
        if len(version1) < len(version2):
            return False
        else:
            return True
a=Solution()
print(a.max_version([["0.1.0", "1.0"], ["2.1.13", "1.20.0"], ["2.1.0", "2.1.0"]]))


d,m,w=[int(i) for i in  input().strip().split()]
i,j,k=[int(i) for i in  input().strip().split()]
weeks=(((k-1)*m+j-1)*d+i-1)%w
end=ord('a')+weeks
print(chr(end))

#  并查集实现查找对应的元素
class unionset(object):
    def __init__(self):
        self.set={}
    def union(self,a,b):
        self.visit(a,b)
        a_root=self.find(a)
        b_root=self.find(b)
        # 合并的时候要兼顾到树的平衡， 如果左边大就将右边的变成左边的节点进行操作
        # 存储可以直接使用map 进行操作
        self.set[a_root]=b_root
    def find(self,a):
        temp=self.set.get(a,None)
        if temp==None:
            return None
        if self.set[a]==a:
            return self.set[a]
        else:
            # 直接将一个树的基本操作
            self.set[a]=self.find(self.set[a])
            return self.set[a]
    def visit(self,a,b):
        for i in [a,b]:
            if self.set.get(i,None)==None:
                self.set[i]=i

    def equal(self,a,b):
        a_root=self.find(a)
        b_root=self.find(b)
        if a_root is None or b_root is None:
            return False
        else:
            return a_root==b_root

n = int(input().strip())
commandlist = []
reason=unionset()
for i in range(n):
    commandlist.append([int(i) for i in input().strip().split()])
    
    
for command in commandlist:    
    if command[0] == 2:
        moda=command[1]%command[3]
        modb=command[2]%command[3]
        if moda==modb:
            res=True
        else:
            res=reason.equal(moda,modb)
        if res:
            print("YES")
        else:
            print("NO")
    elif command[0] == 1:
        reason.union(command[1],command[2])
