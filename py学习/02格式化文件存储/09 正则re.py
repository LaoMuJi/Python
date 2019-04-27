import re

# 查找数字
# compile 将表示正则的字符串编译为一个pattern对象

p = re.compile(r'\d')

# 在字符串里面查找
m = p.match('aaa111bbb222ccc333ddd444')

print(m)

# ——————————————————————————————————————————
print('——————————————————')

p = re.compile(r'\d+')

# 在字符串里面查找，查找起始位置，终止位置
m = p.match('123456789',2,26)

print(m)

# match值
print(m[0])

# 开始、结束 位置
print(m.start(0))
print(m.end(0))

# ——————————————————————————————————————————
print()
print('——————————————————')

# I 表示忽略大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = p.match('I am is LiuChang')
print(m)

print(m.group(0))
print(m.group(2))
print(m.groups())

# ——————————————————————————————————————————
print()
print('—————————查找—————————')

p = re.compile(r'\d+')

# 查找一个
m = p.search('sdhjka23213hjkasdh4213')
print(m.group())

# 查找多个 返回列表
m = p.findall('sdhjka23213hjkasdh4213')
print(m)

# ——————————————————————————————————————————
print()
print('—————————替换—————————')

p = re.compile(r'(\w+) (\w+)')
s = 'I 456 love manman,7788 hehe'
r = p.sub(r'替换替换', s)
print(r)

print()
print('—————————查找中文—————————')
# 查找中文
t = u'大家好，我叫刘畅，hello everybody'
p = re.compile(r'[\u4e00-\u9fa5]+')
r = p.findall(t)
print(r)

