import person_pb2
person =person_pb2.person()
people=person_pb2.people()
number=person_pb2.person.phonenumber()
number.type=2
number.num="60538"
print(number)

# 在proto2 中required  是必填字段, 在proto3 中的应该是可以不填也不会报错， 可以进行自动的处理
# Message people.people is missing required fields: people[0].sex,people[0]

for i in range(10):
    # 使用add 新添加了一个对象， 在go 中数据结构体的格式是可以导出的所以直接声明结构体就可以进行操作， 但是在python 中是声明一个类
    person1=people.personlist.add()
    # add 函数可以添加repeat类型的重复对象
    person1.name="123"
    person1.age=12

strlist=people.SerializeToString()
personlist1=person_pb2.people()
print(personlist1.ParseFromString(strlist))
print(len(personlist1.people))
for i in personlist1.people:
    # 返回的每一个对象都是对应的class, 按照对象的方法进行调用想
    print(i.name,i.age)