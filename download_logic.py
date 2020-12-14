import requests


class down_search():
    def search(SN, PN):
        _SN = SN
        _PN = PN
        print(SN, PN)

        url = 'http://10.167.4.191:8200/api/Deviation/GetDeviationWoBySN?SN=' + SN
        #headers = {'Mozilla/5.0(Windows NT 6.1;Win64;x64)'}
        headers = {
            'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
        }
        try:
            r = requests.get(url, verify=False, headers=headers)
            print(r.status_code)
        except requests.RequestException as e:
            print(e)
