import urllib.request,urllib.parse,json
class start:
    def __init__(self,content):
        self.content = content

    def run(self,content):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        data = {
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '15952984080843',
            'sign': 'cd365dd8fbcb447c3e0c4ed180285872',
            'ts': '1595298408084',
            'bv': '530358e1f56d925c582f7d2d49f07756',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'}

        data = urllib.parse.urlencode(data).encode('utf-8')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        target = json.loads(html)

        print("\n翻译结果:%s\n" % (target['translateResult'][0][0]['tgt']))


while True:
    content = str(input('请输入内容>>>'))
    run = start(content)
    run.run(content)


