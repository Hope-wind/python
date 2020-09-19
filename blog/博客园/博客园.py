from requests import get
from time import time
from parsel import Selector
import re,threading,os
from time import sleep

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

}

proxies = {
    'https':'175.44.109.236:9999'
}


path = os.path.dirname(__file__)
path = path + '/data.csv'
if not os.path.exists(path):
    print("检测到没有容器")
    print('生成完毕' + path)




class data:
    '''初始化'''
    def __init__(self,url,headers):
        self.url = url
        self.headers = headers

    '''属性'''
    def get_data(self):
        '''请求数据'''
        html_data = get(url = self.url,headers = headers).text
        return html_data

    def parse_and_save_data(self,html_data):
        selector = Selector(html_data)
        result_list = selector.xpath('//article[@class="post-item"]')
        for sel in result_list:
            name = sel.css('section > div > a ::text').extract_first() #博客名
            The_author = sel.css('section > footer > a > span ::text').extract_first() #作者
            Release_time = sel.css('section > footer > span.post-meta-item > span ::text').extract_first() #发布时间
            Watch_the_number_of_times = sel.css('section > footer > a:nth-child(5) > span ::text').extract_first() #观看次数
            '''id提取'''
            xpath_parsel_data = sel.xpath('./section/div/a/@href').extract_first()
            split_parsel_data = xpath_parsel_data.split('/p')[-1]
            str_data = re.findall('\d\d\d\d\d*', split_parsel_data)
            praise_id = '#digg_count_' + str_data[0]

            '''url提取'''
            url = sel.xpath('./section/div/a/@href').extract_first() #url

            praise = sel.css(praise_id + '::text').extract_first() #赞
            comments = sel.css('section > footer > a:nth-child(4) > span ::text').extract_first()  #评论数


            data = {
                '博客名':name,
                '作者':The_author,
                '发布时间':Release_time,
                '浏览量':Watch_the_number_of_times,

                '地址':url,
                '赞':praise,
                '评论数':comments,

            }
            with open(path,mode='a+',encoding='utf-8') as f:
                print('写入完成:',data)
                f.write(str(data) + '\n')




def start_save(base_url):
    '''主线程'''
    write_data = data(url=base_url,headers=headers)
    html_data = write_data.get_data()
    write_data.parse_and_save_data(html_data)

def main():
    for page in range(1,201):
        base_url = 'https://www.cnblogs.com/#{}'.format(page)
        print('\n###########正在下载第{}页数据###########\n'.format(page))
        if page > 1:
            sleep(0.5)

        '''线程启动器'''
        my_thread = threading.Thread(target = start_save,args = (base_url,))
        my_thread.setDaemon((True))
        my_thread.start()


if __name__ == '__main__':
    '''启动器'''
    lock = threading.RLock()
    start_time = time()
    main()
    end_time = time()
    use_time = end_time - start_time
    print(use_time)
