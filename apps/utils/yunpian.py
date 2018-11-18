import requests
import json


class Yunpian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            'text': '',
            'mobile': mobile
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        print(re_dict)


if __name__ == '__main__':
    yun_pian = Yunpian('')
    yun_pian.send_sms('2017', '13269463799')
