#encoding: utf-8


import requests

headers = {
        'user-agent': 'adjkasl'
        }

def crawl(key):
    url = 'https://danjuanapp.com/djapi/fund/nav-growth/{}?day=30'.format(key)
    res = requests.get(url,headers=headers)
    if res.status_code ==200:
        data= res.json()
        items= data.get('data').get('fund_nav_growth')
        res_t = []
        res_z =[]
        for i in items:
            times =i.get('date')
            per =i.get('gr_nav')
            res_t.append(times)
            res_z.append(per)
        return {'time':res_t,"price":res_z}
            

#print(crawl())

