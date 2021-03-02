"""
yaml
"""
import yaml
#yaml.load
#转化成列表
print(yaml.load(open("demo.yml"),Loader=yaml.FullLoader))
#转化成字典(a后有空格)
print(yaml.load("""
 a: 1
 """,Loader=yaml.FullLoader))

#yaml.dump
with open("demo2.yml","w") as f:
    print(yaml.dump(data=[['Hesperiidae', 'Papilionidae'], ['Apatelodidae', 'Epiplemidae']],stream=f))