import re

# —————————查找—————————



# re.match(r'.', '', re.S).group()    re.S：.包括反斜杠   re.I表示忽略大小写
m = re.match(r'\d+', '1233zzz42').group()
print(m)



# 查找一个
# p = re.compile(r'\d+')
# m = p.search('sdhjka23213hjkasdh4213')
# print(m.group())



m = re.search(r'\d+', 'sdhjka23213hjkasdh4213').group()
print(m)




# 查找多个 返回列表
m = re.findall(r'\d+', 'sdhjka23213hjkasdh4213')
print(m)

