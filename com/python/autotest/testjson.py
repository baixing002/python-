"""
json 是由字典和列表组成的
"""
import  json

data ={
    "name":["hufeng","nickname"],
    "age":26,
    "gender":"male"
}
#dumps 将json转化成字符串的形式
print(type(data))
data1 = json.dumps(data)
print(data1)
print(type(data1))
#json.loads 将字符串转化成json类型
data2 = json.loads(data1)
print(type(data2))
print(data2)