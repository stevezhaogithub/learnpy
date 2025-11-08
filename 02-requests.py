# requests 是用 Python编写的基于 urllib 的库
# 1. 安装 pip3 install requests

import requests


def test1():
    # 1. requests 基本使用
    res = requests.get('https://www.baidu.com/')
    print(type(res))
    print(res.status_code)
    print(res.text)
    print(res.cookies)



def test2():
    # 2. requests 的其他请求方式
    # 验证 http 请求的验证: https://httpbin.org/
    requests.post('https://httpbin.org/post')
    requests.put('https://httpbin.org/put')
    requests.delete('https://httpbin.org/delete')
    requests.head('https://httpbin.org/get')
    requests.options('https://httpbin.org/get')


# get 请求不带参数
def test3():
    res = requests.get('https://httpbin.org/get')
    print(res.text)
    

# get 请求带参数
def test4():
    data = {
        'name': 'steve',
        'age': 18
    }
    res = requests.get('https://httpbin.org/get', params = data)
    print(res.text)


# 解析 json
def test5():
    res = requests.get('https://httpbin.org/get')
    print(type(res.text))
    # 将返回结果以 json 格式显示
    print(res.json())
    print(type(res.json()))
    
    
# 获取二进制数据
def test6():
    res = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
    print(type(res.text))
    print(type(res.content))
    print(res.text)
    print(res.content)
    
# 获取二进制数据, 并保存到文件
def test7():
    res = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
    with open('./baidu.jpg', 'wb') as f:
        f.write(res.content)
        f.close()
    print('write ok.')

test7()
