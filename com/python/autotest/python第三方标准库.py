"""
requests

"""
import  requests

r1=requests.get("http://www.baidu.com")
r1.encoding='utf-8'
print(r1)
print(r1.status_code)
print(r1.encoding)
print(r1.text)
#
r2 = requests.post('http://httpbin.org/post',data={'key':'value'})
print(r2.text)
