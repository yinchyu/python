import base64
with open("./config.json", "br") as f:
	content =f.read()
	print("原始数据的内容：\n",content)
	encode =base64.b64encode(content)
	#  编码解码后都是二进制的数据， 然后进行操作
	print("------------")
	print("编码后的数据内容:\n",encode)
	with open("./sector_config","wb")as f:
		f.write(encode)
	print("------------")
	decode=base64.b64decode(encode)
	print("解码后的数据内容:\n",decode.decode("utf-8"))
	#按照utf-8的形式输出
	

