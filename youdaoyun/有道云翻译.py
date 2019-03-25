from urllib import request,parse
import time
import hashlib
import json


class youdao(object):
        def __init__(self):
                self.name = input('请输入需要翻译的单词：')
                self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
                self.salt = time.time()*10000
                self.ts = self.salt//10
                self.value = "fanyideskweb" + self.name + str(self.salt) + "p09@Bn{h02_BIEe]$P^nG"
        def getMd5(self,value):
                value=self.value
                md5 = hashlib.md5()
                md5.update(bytes(value,encoding='utf-8'))
                return md5.hexdigest()

        def seal(self):
                self.sign = self.getMd5(self.value)
                data = {'i': self.name,
                        'from': 'AUTO',
                        'to': 'AUTO',
                        'smartresult': 'dict',
                        'client': 'fanyideskweb',
                        'salt': self.salt,
                        'sign': self.sign,
                        'ts': self.ts,
                        'bv': '2ad71fdb7f9cd547d88a6e033d113ffe',
                        'doctype': 'json',
                        'version': '2.1',
                        'keyfrom': 'fanyi.web',
                        'action': 'FY_BY_REALTIME',
                        'typoResult': 'false'
                        }
                data_str = parse.urlencode(data)
                headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length': len(data_str),
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=242377553.75907287; OUTFOX_SEARCH_USER_ID="-1348031489@10.168.11.11"; _ga=GA1.2.1552016970.1547215255; JSESSIONID=aaaegdOBvBusWhOykmzKw; ___rl__test__cookies=1550915765147',
                'Host': 'fanyi.youdao.com',
                'Origin': 'http://fanyi.youdao.com',
                'Referer': 'http://fanyi.youdao.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                }
                self.req = request.Request(url=self.url,headers=headers,data=bytes(data_str,encoding='utf-8') )
        def S_response(self):
                try:
                        contents = request.urlopen(self.req).read().decode('utf-8')
                        conontent = json.loads(contents)
                        con=conontent['smartResult']['entries']
                except:
                        contents = request.urlopen(self.req).read().decode('utf-8')
                        conontent = json.loads(contents)
                        con = conontent["translateResult"]["tgt"]
                finally:
                        print(con)
if __name__ == '__main__':
        while True:
                yd=youdao()
                yd.seal()
                yd.S_response()
