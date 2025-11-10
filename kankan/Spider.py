import urllib.request as r
import re
import ssl
import requests
import random
import os
import time


# 获取网页源代码
def get_html(url):
    ssl_context = ssl._create_unverified_context()
    # 定制一个User-Agent请求头变量，请求头字段可以通过百度搜索一个或者使用本地burpsuite抓包复制本地浏览器的请求头
    UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = r.Request(url=url, headers=UA)
    # 用形参=实参的方式传递参数，避免参数位置混乱
    response = r.urlopen(request, context=ssl_context)
    html = response.read()
    return html


# 从网页源代码中抓取图片的 url
def get_imagelist(html):
    # 正则表达式
    pattern = "https://hw-chapter2.kaimanhua.com/comic/S/[a-zA-Z0-9_\-\%/\.]+\?auth_key=[0-9a-zA-Z\-_]+"
    image_url = re.findall(pattern, str(html))
    imageurl_list = []  # 定义一个空列表用来存储图片完整路径
    for i in image_url:  # 用for i in 循环结构来遍历图片路径列表并对其进行处理
        imageurl_list.append(i)  # 每次进入循环，都对列表元素拼接url前缀生成一个完整的图片地址列表
    return imageurl_list  # 返回图片完整路径列表


def req_image(img_url):
    # 常见的 Browser User Agents 10 个
    user_agents = [
        # Chrome on Windows
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        # Chrome on macOS
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        # Firefox on Windows
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        # Firefox on macOS
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0",
        # Safari on macOS
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
        # Safari on iOS (iPhone)
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
        # Chrome on Android
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.90 Mobile Safari/537.36",
        # Microsoft Edge on Windows
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        # Chrome on Linux
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        # Samsung Internet on Android
        "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36"
    ]

    # 产生一个 [0, 9] 的随机数
    rdm = random.randint(0, 9)
    headers = {
        'Host': 'hw-chapter2.kaimanhua.com',
        'User-Agent': user_agents[rdm],  # 随机使用一个 user-agents
        'Accept': 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://www.kanman.com/',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=5, i',
    }
    response = requests.get(
        url=img_url,  # 直接使用完整的 URL
        headers=headers,
    )
    return response.content


# 根据图片 url 下载图片
def download_image(imageurl_list, N):
    # 创建用于存储图片的目录
    if not os.path.exists("kkpics1"):
        os.makedirs("kkpics1")

    "传入图片url列表，并完成遍历下载"
    num = 0  # 自定义图片编号，在保存图片做重命名时更加清晰
    for i in imageurl_list:
        # 随机延迟 1-3 秒
        delay = random.uniform(1, 3)
        time.sleep(delay)
        
        # 每下载10张图片休息长一点
        if num > 0 and num % 10 == 0:
            time.sleep(5)
        
        num += 1
        # 下载图片
        imagebytes = req_image(i)
        # 将图片保存到本地
        with open("./kkpics1/%03d_%03d.jpg" % (N, num), "wb") as f:  # %03d用于补位替换整数变量，注意提前创建pic目录
            f.write(imagebytes)
        # 打印进度条
        print("#", end="", flush=True)
    print("")




if __name__ == "__main__":
    for i in range(1, 21):
        url = "https://www.kanman.com/107490/" + str(i) + ".html"
        # 1. 获取网页二进制源码，用于抓取并生成图片路径列表
        html = get_html(url)

        # 2. 通过正则表达式抓取其中的图片地址到 list 中
        imageurl_list = get_imagelist(html)

        # 3. 图片总数
        total = len(imageurl_list)
        print(f"开始下载{i}.html网页的 {total} 张图片:")

        # 4. 根据图片路径下载图片
        download_image(imageurl_list, i)
    print("爬虫完成！请在当前执行python命令目录下的 kkpics 文件夹下观察爬虫结果！")





################### 下面是代码备份

#
#def req_image(img_url):
#    pattern = r'(.*?)\?auth_key=([^&]+)'
#
#    match = re.search(pattern, img_url)
#    url_part = match.group(1)  # ?auth_key前面的URL部分
#    auk = match.group(2)  # auth_key值
#
#    # 常见的 Browser User Agents 10 个
#    user_agents = [
#        # Chrome on Windows
#        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#        # Chrome on macOS
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#        # Firefox on Windows
#        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
#        # Firefox on macOS
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0",
#        # Safari on macOS
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
#        # Safari on iOS (iPhone)
#        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
#        # Chrome on Android
#        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.90 Mobile Safari/537.36",
#        # Microsoft Edge on Windows
#        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
#        # Chrome on Linux
#        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#        # Samsung Internet on Android
#        "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36"
#    ]
#
#    # 产生一个 [0, 9] 的随机数
#    rdm = random.randint(0, 9)
#    headers = {
#        'Host': 'hw-chapter2.kaimanhua.com',
#        'User-Agent': user_agents[rdm],  # 随机使用一个 user-agents
#        'Accept': 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
#        'Accept-Language': 'en-US,en;q=0.5',
#        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
#        'Connection': 'keep-alive',
#        'Referer': 'https://www.kanman.com/',
#        'Sec-Fetch-Dest': 'image',
#        'Sec-Fetch-Mode': 'no-cors',
#        'Sec-Fetch-Site': 'cross-site',
#        'Priority': 'u=5, i',
#        # Requests doesn't support trailers
#        # 'TE': 'trailers',
#        # 'X-Forwarded-For': '127.0.0.1',
#    }
#    params = {
#        'auth_key': auk,
#    }
#
#    response = requests.get(
#        url=url_part,
#        params=params,
#        headers=headers,
#    )
#    return response.content
#
