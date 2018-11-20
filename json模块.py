#json，轻量级的数据格式，python自带模块
#dumps是处理字符串，dump是处理文件
#json.loads  也是处理字符串
import  json
user = {
    "username":"which",
    "age":18,
    "language":['java','python'],
    "marry":False
}
print(user)   #字典会自动变为单引号。
a = json.dumps(user,indent=3,separators=(',',':'))  #indent是缩进的意思，separators是减少空格，以逗号冒号替换
print(a)      #变为前端能识别的json格式。

a = json.loads(a)     #转为python能识别的json数据格式
print(a)

#写入文件
with  open('tmp.json','w+') as f:
    json.dump(user,f,indent=4,sort_keys=True,separators=(',',':'))

#读入文件
with open('tmp.json')  as  f:
    data = json.load(f)
print(data)




