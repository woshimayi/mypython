'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: 4K_top50.py
@time: 2025/02/23 11:50
@desc: 
'''


import requests
from bs4 import BeautifulSoup

def scrape_top50_movies(url):
    """
    从 4khdr 网站抓取 TOP50 电影榜单。

    Args:
        url (str): 4khdr 网站的首页 URL。

    Returns:
        list: 包含 TOP50 电影名称的列表，如果抓取失败则返回 None。
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = response.apparent_encoding # 设置正确的编码，避免中文乱码
        soup = BeautifulSoup(response.text, 'html.parser')

        # 定位到 TOP50 电影榜单的区域
        # 根据网站 HTML 结构，榜单通常在一个特定的 div 或 ul 列表中
        # 您需要检查网页源代码来确定正确的选择器
        # 经过查看网页源代码，TOP50 榜单似乎在 class 为 "list-ranking" 的 div 中
        ranking_list = soup.find('div', class_='list-ranking')
        if not ranking_list:
            print("未找到 TOP50 电影榜单区域。请检查网站结构是否更新。")
            return None

        movie_names = []
        # 在榜单区域内查找电影名称
        # 电影名称通常在 <a> 标签内，或者在列表项 <li> 内的某个标签里
        # 经过查看网页源代码，电影名称在 <li> 标签内的 <a> 标签的 title 属性中
        movie_items = ranking_list.find_all('li') # 获取所有电影列表项
        for item in movie_items:
            a_tag = item.find('a') # 查找 <a> 标签
            if a_tag and 'title' in a_tag.attrs: # 确保找到 <a> 标签且有 title 属性
                movie_name = a_tag['title']
                movie_names.append(movie_name)

        return movie_names

    except requests.exceptions.RequestException as e:
        print(f"请求网站时发生错误: {e}")
        return None
    except Exception as e:
        print(f"抓取数据时发生错误: {e}")
        return None

if __name__ == '__main__':
    website_url = 'https://www.4khdr.cn/index.php'
    top50_movies = scrape_top50_movies(website_url)

    if top50_movies:
        print("本季度热门电影 TOP50 电影榜单:")
        for index, movie in enumerate(top50_movies, start=1):
            print(f"{index}. {movie}")
    else:
        print("未能成功抓取 TOP50 电影榜单。")

if __name__ == '__main__':
    print('Hello world')
