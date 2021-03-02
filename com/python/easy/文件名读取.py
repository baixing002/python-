import os

path1 ='/home/python-class/lesson1-2/work/5月员工照'
path2 ='/home/python-class/lesson1-2/work/6月员工照'

filename1=os.listdir(path1)
filename2=os.listdir(path2)

print (filename1+filename2)

