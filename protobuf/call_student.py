import student_pb2

data =open("dump_file","rb").read()
res=student_pb2.StudentList()

## student,还针的是一个非导出的对象， 只能在res中使用
res.ParseFromString(data)
#  只要嵌套的下一级是 message 就会生成对应的add 方法进行操作
res2=res.TargetList.add()
res2.name="good"
res2.male=True
print("========",dir(res2.scores))
# append 方法是可以用的， 刚才陷入到了什么漩涡中, 一个重复字段 repeat 一般来说都是使用list 进行操作
res2.scores.append(12)
res2.scores.append(13)
res2.scores.append(15)
print(type(res.Student),res.Student)
# 定义的是describe 的描述信息
print(type(res),type(res.TargetList[0]),res.TargetList[0])
print(type(res.TargetList[0].scores),res.TargetList[0].scores[0])
print(type(res.TargetList[0].scores),res.TargetList)

# data=res.SerializeToString()
# c=open("newdump","ab+")
# c.write(data)
# c.close()

enumitem=student_pb2.HOME
print(enumitem)

mapss=student_pb2.MyMessage()

mapss.mapfield[1]=12
mapss.mapfield[2]=15
print(mapss)





