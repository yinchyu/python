import itertools


c = itertools.cycle("abc")

for i in range(100):
	print(i)
	# 尝试在内存直接列出所有的迭代对象，方便数据处理

