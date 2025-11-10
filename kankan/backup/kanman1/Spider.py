# 经过优化后的代码
import requests
import re
import random
import os
import ssl
import urllib3


# 禁用SSL警告 - 必须在导入后立即执行
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_html(url):
    """
    获取网页源代码
    
    Args:
        url: 要请求的网页URL
        
    Returns:
        bytes: 网页的二进制内容
    """
    # 设置请求头，模拟浏览器访问
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求并获取响应，禁用SSL证书验证
    response = requests.get(url, headers=headers, verify=False)

    return response.content


def get_imagelist(html):
    """
    从网页源代码中提取图片URL列表
    
    Args:
        html: 网页源代码（二进制格式）
        
    Returns:
        list: 包含所有图片URL的列表
    """
    # 正则表达式模式，匹配图片URL
    pattern = "https://hw-chapter2.kaimanhua.com/comic/S/[a-zA-Z0-9_\-\%/\.]+\?auth_key=[0-9a-zA-Z\-_]+"

    # 使用正则表达式查找所有匹配的图片URL
    image_url = re.findall(pattern, str(html))

    # 将匹配到的URL转换为列表
    imageurl_list = []
    for url in image_url:
        imageurl_list.append(url)

    return imageurl_list


# 根据图片路径下载图片
def req_image(img_url):
    """
    请求图片数据
    
    Args:
        img_url: 图片的完整URL
        
    Returns:
        bytes: 图片的二进制数据
    """
    # 常见的浏览器User-Agent列表，用于随机选择
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36"
    ]

    # 随机选择一个User-Agent
    rdm = random.randint(0, 9)

    # 设置请求头
    headers = {
        'Host': 'hw-chapter2.kaimanhua.com',
        'User-Agent': user_agents[rdm],
        'Accept': 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://www.kanman.com/',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=5, i',
    }
    # 直接使用完整的图片URL发送请求
    response = requests.get(img_url, headers=headers, verify=False)

    return response.content


def download_image(imageurl_list, N):
    """
    下载图片并保存到本地
    
    Args:
        imageurl_list: 图片URL列表
        N: 网页编号，用于文件名前缀
    """
    # 创建存储图片的目录
    if not os.path.exists("kkpics"):
        os.makedirs("kkpics")

    num = 0  # 图片计数器
    for img_url in imageurl_list:
        num += 1

        # 下载图片数据
        imagebytes = req_image(img_url)

        # 保存图片到本地，文件名格式：网页编号_图片编号.jpg
        filename = f"./kkpics/{N:03d}_{num:03d}.jpg"
        with open(filename, "wb") as f:
            f.write(imagebytes)

        # 打印进度指示
        print("#", end="", flush=True)

    print("")  # 换行


if __name__ == "__main__":
    # 遍历多个网页进行图片爬取
    for i in range(1, 21):
        # 构造目标网页URL
        url = f"https://www.kanman.com/107490/{i}.html"

        # 1. 获取网页源代码
        html = get_html(url)

        # 2. 提取图片URL列表
        imageurl_list = get_imagelist(html)

        # 3. 统计图片数量
        total = len(imageurl_list)
        print(f"开始下载{i}.html网页的 {total} 张图片:")

        # 4. 下载所有图片
        download_image(imageurl_list, i)

    print("爬虫完成！请在当前执行python命令目录下的 kkpics 文件夹下观察爬虫结果！")
