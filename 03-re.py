# 正则表达式
# 正则表达式测试: https://tool.oschina.net/regex
# 1. re.match(pattern, string, 匹配模式)
# 2. re.findall()
# 3.
# 贪婪模式 \d+ \d*
# 非贪婪模式 \d+? \d*?


import re

# re.match(), match() 只找第一个匹配, 不找全部匹配
# re.match(pattern, string)
# re.findall() 查找所有的匹配
def test01():
    s = "我的邮箱steve_zhao@163.com，他的邮箱zxh@gmail.com."
    pattern = "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
    result = re.match(pattern, s)
    print(result)
    
    
test01()




