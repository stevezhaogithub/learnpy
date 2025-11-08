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
    

# 添加 headers 的请求
def test8():
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    res = requests.get("https://www.zhihu.com/explore", headers = headers)
    print(res.text)



# post 请求 - form data
def test9():
    data = {
        "name":"steve",
        "age":18
    }
    headers = {
        
    }
    res = requests.post("https://httpbin.org/post", data = data, headers = headers)
    print(res.text)
    print("------------------------------")
    print(res.json())

# https://www.ldoceonline.com/dictionary/hello
def test10():
    data = {
        
    }
    # doesn't work
    res = requests.get("https://www.ldoceonline.com/dictionary/hello")
    print(res.json())



# response 的属性
def test11():
    headers = {
    "Host": "www.jianshu.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:144.0) Gecko/20100101 Firefox/144.0",
    "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Referer": "https://www.jianshu.com/",
    "Cookie": "signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2; locale=zh-CN; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219a6198ddde1b0-05e3f6cce51c3e-442a2830-1484784-19a6198dddf865%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219a6198ddde1b0-05e3f6cce51c3e-442a2830-1484784-19a6198dddf865%22%7D; sajssdk_2015_cross_new_user=1; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1762574000; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1762574000; HMACCOUNT=539459E115FADE9E",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=5",
    "TE": "trailers"
    }
    
    for i in range(1,1000):
        res = requests.get("https://www.jianshu.com/", headers = headers)
        print(res.status_code)
#    print(res.headers)
#    print(res.cookies)
#    print(res.url)
#    print(res.history)
#    print(res.text)


test11()
