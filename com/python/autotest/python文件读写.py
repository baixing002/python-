"""
文件的读写
"""

# print(open('data.txt'))
# f = open('data.txt')
# #可读
# print(f.readable())
#读取文件中的所有数据(所有的行全都读取出来了)
# print(f.readlines())
# 逐行读取
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
#with的用法(不需要执行close()的操作)
#with语句块，可以将文件打开之后，操作完毕，自动关闭这个文件（对with的操作 一定要在with的语句块里）
#图片读取需要使用rb,读取二进制的格式
#正常的文本，可以使用rt,也就是它的的默认格式
with open('data.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    # print(f.readline())
    # print(f.readlines())