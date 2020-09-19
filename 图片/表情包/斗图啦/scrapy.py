import asyncio,aiohttp,os
from parsel import Selector
from time import time


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}


path = os.path.dirname(__file__)
path = path + '/image'
if not os.path.exists(path):
    print('检测到没有容器')
    os.mkdir(path)
    print('生成完毕' + path)


class Download(object):

    def mk_url(self,startnum,endnum):
        for num in range(startnum,endnum+1):
            base_url = 'https://www.doutula.com/photo/list/?page={}'.format(num)
            task_list = []
            task_list.append(base_url)
            yield task_list




    async def fetch_html(sef,session,url):
        '''请求网页数据'''
        async with session.get(url) as response:
            return await response.text()

    async def fetch_img(sef,session,url):
        '''请求图片数据'''
        async with session.get(url) as data:
            return await data.read()

    async def parse_data(self,session,html):
        '''处理数据'''
        selector = Selector(html)
        result_list = selector.xpath('//a[@class="col-xs-6 col-sm-3"]')

        for result in result_list:
            img_url = result.xpath('./img/@data-original').extract_first()
            img_title = result.xpath('./img/@alt').extract_first()

            all_title = img_title + '.' + img_url.split('.')[-1]

            content = await self.fetch_img(session,img_url)

            try:
                with open(path + "\\" + all_title,mode='wb') as f:
                    print("下载完成:",all_title)
                    f.write(content)

            except Exception as e:
                print(e)


    async def start_save(self,url):
        async with aiohttp.ClientSession(headers=headers) as session:
            html = await self.fetch_html(session,url)
            await self.parse_data(session = session, html = html)

    async def download_pictures(self,startnum,endnum):
        for page in range(startnum,endnum+1):
            print("######正在下载第{}页数据######".format(page))
            url_list = self.mk_url(startnum,endnum)
            for url in url_list:
                base_url = url[0]
                await self.start_save(base_url)


'''实例化'''
if __name__ == '__main__':
    print("任务启动中...")
    download = Download()
    loop = asyncio.get_event_loop()

    tasks = [
        asyncio.ensure_future(download.download_pictures(1,2000)),
        asyncio.ensure_future(download.download_pictures(2001, 4000)),
        asyncio.ensure_future(download.download_pictures(4001, 6000))
    ]
    start_time = time()
    loop.run_until_complete(asyncio.gather(*tasks))
    end_time = time()
    run_time = end_time - start_time
    print(run_time)
