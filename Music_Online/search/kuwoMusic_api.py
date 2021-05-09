# -*- coding: utf-8 -*-
# author: jiuwei1997
# description:破解酷我音乐网站
# date:2021-5-9
import requests


def get_music_info(key_word):
    url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={key_word}&pn=1&rn=30&httpsStatus=1&reqId=85275eb0-b0d3-11eb-b9c3-2f7abb817827'
    headers = {
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1620570727; _ga=GA1.2.2058493930.1620570727; _gid=GA1.2.1175609155.1620570727; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1620570776; kw_token=HI9EQMS9PCA; _gat=1',
        'csrf': 'HI9EQMS9PCA',
        'Referer': 'http://www.kuwo.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',

    }
    resp = requests.get(url, headers=headers)
    # 获取到搜索结果的音乐信息数据集合
    music_message = resp.json()["data"]["list"]
    music_info = []
    # 遍历音乐数据集合，获取歌曲的名字和播放链接地址
    for message in music_message:
        music_name = message["name"]
        music_rid = message["rid"]
        # 通过免费歌曲的播放地址来获取付费歌曲的播放地址（破解方法：替换歌曲的rid）
        music_play_url = f'http://www.kuwo.cn/url?format=mp3&rid={music_rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1620572010467&httpsStatus=1&reqId=51acc860-b0d6-11eb-b9c3-2f7abb817827'
        resp = requests.get(music_play_url, headers=headers)
        real_music_play_url = resp.json()["url"]
        # 将获取到的歌曲信息构造成一个字典添加到列表传给前端
        music_info_dict = {
            'music_name': music_name,
            'music_play_url': real_music_play_url
        }
        music_info.append(music_info_dict)
    return music_info

if __name__ == '__main__':
    music_info = get_music_info("周杰伦")
    print(music_info)


