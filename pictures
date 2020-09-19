from parsel import Selector
from random import randint
from time import time
import os,aiohttp,asyncio


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

}

path = os.path.dirname(__file__)
path = path + '/image'
if not os.path.exists(path):
    print('检测到没有容器')
    os.mkdir(path)
    print("生成完毕" + path)




class Download(object):

    def mk_url(self,startnum,endnum):
        '''生成url'''
        for _ in range(startnum,endnum+1):
            base_url = 'https://anime-pictures.net/pictures/view_posts/{}?lang=en'.format(_)
            task_list =[]
            task_list.append(base_url)
            return task_list

    async def fetch_html(self,session, url):
       '''请求网页数据'''
       async with session.get(url) as response:
           return await response.text()

    async def fetch_img_data(self,session,url):
        '''请求图片数据'''
        async with session.get(url) as data:
            return await data.read()

    async def parser_data(self,session,html):
        '''处理数据'''
        selector = Selector(html)
        result_list = selector.xpath('//span[@class="img_block_big"]')

        for result in result_list:
            image_url = result.xpath('./a/picture/source/img/@src').extract_first()
            img_url = 'https:' + image_url  # 手动拼url
            content = await self.fetch_img_data(session,img_url)

            id = str(randint(0,99999999999999))
            try:
                with open(path + '\\' + id + os.path.splitext(img_url)[1], mode='wb') as f:
                    f.write(content)
                    print('保存完成',id)
            except Exception as e:
                print(e)

    async def start_save(self,url):
        async with aiohttp.ClientSession(headers=headers) as session:
            html = await self.fetch_html(session, url=url)
            await self.parser_data(session=session, html=html)

    # base_url = 'https://anime-pictures.net/pictures/view_posts/0?lang=en'

    async def download_pictures(self,startnum,endnum):
        for page in range(startnum,endnum+1):
            print("######正在下载第{}页数据######".format(page))
            url_list = self.mk_url(startnum,endnum)
            for url in url_list:
                base_url = url
                await self.start_save(base_url)

'''实例化'''
if __name__ == '__main__':
    print('任务启动中...')
    download = Download()
    loop = asyncio.get_event_loop()
    s_time = time()
    tasks = [
        asyncio.ensure_future(download.download_pictures(1,2000)),
        asyncio.ensure_future(download.download_pictures(2001,4000)),
        asyncio.ensure_future(download.download_pictures(4001, 6000))
    ]
    loop.run_until_complete(asyncio.gather(*tasks))
    e_time = time()
    print('用时:',e_time - s_time,'秒')
