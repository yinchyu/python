import collections
import requests

counter = 0


def func1():
    import copy
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


def func2():
    global counter
    """
    马走日的位置，使用回溯然后判断位置
    :return:
    """
    x0, y0, x1, y1 = [int(i) for i in input().strip().split()]

    def dfs(_x, _y, _x1, _y1):
        global counter
        if _x == _x1 and _y == _y1:
            counter += 1
        for step in [[2, 1], [1, 2]]:
            if _x + step[0] <= _x1 and _y + step[1] <= _y1:
                dfs(_x + step[0], _y + step[1], _x1, _y1)

    dfs(x0, y0, x1, y1)
    print(counter)


class Cmp:
    def __init__(self):
        self.flag = False

    def cmp(self, g1, g2, records):
        # write code here
        self.dfs(g1, g2, records)
        if self.flag:
            return 1
        self.dfs(g2, g1, records)
        if self.flag:
            return -1
        return 0

    def dfs(self, g1, g2, records):
        if g1 == g2:
            self.flag = True
            return
        for group in records:
            if group[0] == g1:
                self.dfs(group[1], g2, records)


def func3():
    a = Cmp()
    res = a.cmp(1, 3, [[3, 2], [2, 4], [2, 1], [4, 1]])
    print(res)
    print({1, 3, 2} == {12, 3, 3})


class Solution:
    def max_version(self, version_list):
        res = []
        for version in version_list:
            first = [int(i) for i in version[0].strip().split(".")]
            second = [int(i) for i in version[1].strip().split(".")]
            if self.compare(first, second):
                res.append(1)
            else:
                res.append(2)
        return res

    @staticmethod
    def compare(version1, version2):
        n = len(version1) if len(version1) < len(version2) else len(version2)
        for i in range(n):
            if version1[i] > version2[i]:
                return True
            elif version1[i] == version2[i]:
                continue
            else:
                return False
            # 如果第二个的长度比第一个的长度长，就认为第二个的版本高
        if len(version1) < len(version2):
            return False
        else:
            return True


def func4():
    a = Solution()
    print(a.max_version([["0.1.0", "1.0"], ["2.1.13", "1.20.0"], ["2.1.0", "2.1.0"]]))

def func5():

    datalist = [int(i) for i in input().strip().split()]
    left, right = 0, len(datalist) - 1

    while right > 0:
        if datalist[right] > datalist[right - 1]:
            right -= 1
        else:
            break

    while left < right:
        if datalist[left] < datalist[right]:
            left += 1
        else:
            break
    print(left + 1, right + 1)
    string = "[[[]]]"
    stack = [0]
    for i in range(len(string)):
        if string[i] == '[':
            stack.append(1)
        elif string[i] == ']':
            if i + 1 < len(string) and string[i + 1].isnumeric():
                times = int(string[i + 1])
                stack.append(times * stack.pop())
            else:
                stack.append(stack.pop() + stack.pop())
    print(stack.pop())


class LRUCache(collections.OrderedDict):
    def __init__(self, capacity: int):
        # 对父类进行初始化
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        # 更改元素的使用频率
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


def func7():
    def getinfo():
        req = requests.request("GET", "https://www.baidu.com")
        if req.status_code == 200:
            print(req.content)
            with open("a.html", "a+") as f:
                f.write(str(req.content.decode("utf-8", errors="ignore")))

    getinfo()


def func8():
    """阿里面试第一题，一个月份的位置判断"""
    d, m, w = [int(i) for i in input().strip().split()]
    i, j, k = [int(i) for i in input().strip().split()]
    weeks = (((k - 1) * m + j - 1) * d + i - 1) % w
    end = ord('a') + weeks
    print(chr(end))


class UnionSet(object):
    def __init__(self):
        self.set = {}

    def union(self, a, b):
        self.visit(a, b)
        a_root = self.find(a)
        b_root = self.find(b)
        # 合并的时候要兼顾到树的平衡， 如果左边大就将右边的变成左边的节点进行操作
        # 存储可以直接使用map 进行操作
        self.set[a_root] = b_root

    def find(self, a):
        temp = self.set.get(a, None)
        if temp is None:
            return None
        if self.set[a] == a:
            return self.set[a]
        else:
            # 直接将一个树的基本操作
            self.set[a] = self.find(self.set[a])
            return self.set[a]

    def visit(self, a, b):
        for i in [a, b]:
            if self.set.get(i, None) is None:
                self.set[i] = i

    def equal(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root is None or b_root is None:
            return False
        else:
            return a_root == b_root


def func9():
    """
     阿里第二题，判断两个元素是否是相连的
    :return:
    """
    n = int(input().strip())
    commandlist = []
    reason = UnionSet()
    for i in range(n):
        commandlist.append([int(i) for i in input().strip().split()])

    for command in commandlist:
        if command[0] == 2:
            moda = command[1] % command[3]
            modb = command[2] % command[3]
            if moda == modb:
                res = True
            else:
                res = reason.equal(moda, modb)
            if res:
                print("YES")
            else:
                print("NO")
        elif command[0] == 1:
            reason.union(command[1], command[2])


def func1():
    """
    美团面试 在小美给出的 n 个整数中，恰好有 k 个数严格比 x 小
    :return:
    """
    line = int(input().strip())
    nklist = []
    numlist = []
    for i in range(line):
        n, k = [int(i) for i in input().strip().split()]
        nums = [int(i) for i in input().strip().split()]
        # 排序操作
        nums.sort()
        numlist.append(nums)
        nklist.append([n, k])
        #时间复杂度是o(n)
    for i in range(line):
        n, k = nklist[i]
        nums = numlist[i]
        #  直接返回一个1 就可以， 估计没有通过可能有这个原因
        if k - 1 == 0:
            res = 1
        else:
            res = nums[k - 1] + 1
        print(nums, res)
        if 1 <= res <= n:
            print("YES")
            print(res)
        else:
            print("NO")


def func2():
    string_func2 = input().strip()
    res = []
    lasstr = ""
    string_func2 = string_func2.replace(" ", "")
    i = 0
    n = len(string_func2)
    while i < n:
        if i - 1 >= 0 and string_func2[i] != lasstr:
            res.append(string_func2[i])
            lasstr = string_func2[i]
        elif i - 1 < 0:
            res.append(string_func2[i])
            lasstr = string_func2[i]
        i += 1

    print("".join(res))

def func2better():
    """
    增加一个前缀符，就省去了索引下标合法性的判断
    :return:
    """
    string_func2 = input().strip()
    res = []
    lasstr = "$"
    for i in string_func2:
        if i!=" " and i!=lasstr:
            res.append(i)
            lasstr=i
    print("".join(res))
def func3():
    """'
    找出前边比该元素小的最大的元素
    能够优化的地方在查找的地方， 不使用顺序查找， 使用二分查找进行操作
    """
    n = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    prev = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] > prev[i]:
                prev[i] = nums[j]
    _sum = 0
    for i in range(n):
        _sum += (i + 1) * prev[i]


def func31():
    import heapq
    heaps = []
    n = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    heapq.heappush(heaps, nums[0])
    for i in range(1, n):
        print(i)


def func4():
    """
    找到最小的元素替换的个数，
    :return:
    """
    n = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    res = {}
    for i in range(n // 2):
        if nums[i] != nums[i + n // 2]:
            key = (nums[i], nums[i + n // 2])
            res[key] = 1
    print(len(res.keys()))


def func13():
    """
    版本号比较， 前边大返回1 后边大返回-1  相等返回0
    :return:
    """
    versiona, versionb = [i for i in input().strip().split()]
    alist = versiona.split(".")
    blist = versionb.split(".")

    def compare(_alist, _blist):
        n1 = len(_alist)
        n2 = len(_blist)
        for i in range(max(n1, n2)):
            i1 = int(_alist[i]) if i < n1 else 0
            i2 = int(_blist[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0

    print(compare(alist, blist))


def func15():
    numlist = [int(i) for i in input().strip().split()]
    numlist.sort()
    n = len(numlist)
    res = []
    for first in range(n):
        if first > 0 and numlist[first] == numlist[first - 1]:
            continue
        thrid = n - 1
        target = -numlist[first]
        for second in range(first + 1, n):
            if second > first + 1 and numlist[second] == numlist[second - 1]:
                continue
            while second < thrid and numlist[second] + numlist[thrid] > target:
                thrid -= 1
            if second == thrid:
                break
            if numlist[second] + numlist[thrid] == target:
                res.append([numlist[first], numlist[second], numlist[thrid]])

    for i in res:
        print(" ".join([str(j) for j in i]))


def func6():
    """
    计算圆和坐标轴相交的位置
    :return:
    """
    lines = int(input().strip())
    nums = []
    for i in range(lines):
        nums.append([int(i) for i in input().strip().split()])

    for num in nums:
        x, y, r = num
        x = abs(x)
        y = abs(y)
        if r >= x:
            if r >= y:
                if x * x + y * y > r * r:
                    print(2)
                elif x * x + y * y == r * r:
                    print(3)
                else:
                    print(4)
            else:
                print(1)
        else:
            if r >= y:
                print(1)
            else:
                print(0)


def func16():
    """
    计算糖果的范围， 要有连续的糖果
    :return:
    """
    n, t, c = [int(i) for i in input().strip().split()]
    nums = [int(i) for i in input().strip().split()]
    _counter = 0
    start = 0
    end = 0
    while end < n:
        while start <= (n - c):
            for j in range(start, start + c):
                if nums[j] > t:
                    start = j + 1
                    break
            else:
                _counter += 1
                break
        end = start + c
        while end < n:
            if nums[end] <= t:
                _counter += 1
            else:
                start = end + 1
                break
            end += 1

    print(counter)


def stackvisit(strings):
    """
    如果没有匹配完到就返回栈剩余元素长度，如果匹配完就返回嵌套的深度
    :param strings:
    :return:
    """
    newstack = []
    deep = 0
    for i in strings:
        if i == "(":
            newstack.append(i)
            if len(newstack) > deep:
                deep = len(newstack)
        if i == ")":
            if len(newstack) > 0:
                temp = newstack[-1]
                if temp == "(":
                    newstack.pop()
                elif temp == ")":
                    newstack.append(i)
            elif len(newstack) == 0:
                newstack.append(i)
    if len(newstack) == 0:
        return deep
    else:
        return -len(newstack)


def func11():
    """
    拼多多第三题
    nums = int(input().strip())
    _string=input().strip()
    :return:
    """

    _string = "R))LL(((RR)"
    strlist = list(_string)
    stack_queue = []
    res = []
    pointer = 0
    for i in strlist:
        if i == "L":
            pointer -= 1
            if pointer < 0:
                pointer = 0
            if len(res) > 0:
                res.append(res[-1])
            else:
                res.append(0)
        elif i == "R":
            pointer += 1
            if 0 < len(stack_queue) <= pointer:
                pointer = len(stack_queue) - 1
            elif pointer >= len(stack_queue) == 0:
                pointer = 0
            if 0 <= pointer - 1 < len(res):
                res.append(res[pointer - 1])
            else:
                res.append(0)
        elif i == "D":
            stack_queue = stack_queue[:pointer] + stack_queue[pointer + 1:]
            res.append(stackvisit("".join(stack_queue)))
        elif i == "(":
            stack_queue.insert(pointer, "(")
            pointer += 1
            res.append(stackvisit("".join(stack_queue)))
        elif i == ")":
            stack_queue.insert(pointer, ")")
            pointer += 1
            res.append(stackvisit("".join(stack_queue)))
    print(res)


def func12():
    # 集合的用法
    a={1,2,3,4,5,6}
    a.add(15)
    print(a)

def  func13():
    import heapq
    a=[9,23,5,2,1]
    heapq.heapify(a)
    print(a)
    heapq.heappush(a,0)
    print(a)
    #把在数据进堆的时候把所有数据都去相反数就可以啦
    #秒哇，这都没有想到，真的是日了狗，自己的思想太单纯
    for i in range(len(a)):
        item=heapq.heappop(a)
        print(item)



func13()