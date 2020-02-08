import json
import os
import requests
from googletrans import Translator


# def get_chinaDayList():
#     with open(os.path.join('data','data.json'),'r',encoding='utf-8') as f:
#         data = json.load(f)
#         #chinaDayList = data['chinaDayList']     #结果为list,{'date': '01.13', 'confirm': '41', 'suspect': '0', 'dead': '1', 'heal': '0'}
#         # date = [x['date'] for x in chinaDayList]
#         # confirm = [x['confirm'] for x in chinaDayList]
#         # suspect = [x['suspect'] for x in chinaDayList]
#         # dead = [x['dead'] for x in chinaDayList]
#         # heal = [x['heal'] for x in chinaDayList]
#         chinadata = data['areaTree'][0]['children']     #全国数据，结果为列表
#         pro = []
#         for i in chinadata:
#             pro.append(i['name'])

#         print(pro)
#         #print(chinadata[0])
#         #print(type(chinadata[0]))
#     return chinadata

# def fanyi():
#     a = ['湖北','西藏']
#     translate = Translator()
#     b = []
#     for i in a:
#         b.append(translate.translate(i).text)
#     print(b)
#     # c = 'hello world'
#     # d = ['hello','world']
#     # for i in d:
#     #     m = i
#     #     print(m)
#     #     a = iciba(m,dst = 'zh')
#     #     print(a)



def themeriver():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    r_data = json.loads(requests.get(url).text)
    data = json.loads(r_data['data'])    #初始化json数据，为dict ['chinaTotal']
    #print(data['areaTree'][0]['children'][0])
    translate = Translator()
    country = []    #中文国家提取
    print(translate.translate(data))
    # total_confirm = []
    # for i in data['areaTree']:
    #     country.append(i['name'])
    #     total_confirm.append(i['total']['confirm']) 
    # countryEN = []  #翻译
    # for i in country:
    #     countryEN.append(translate.translate(i).text)
    print(country)
    #print(countryEN)

def demo():
    zidian = {}
    with open('guojia.json','r',encoding='utf-8') as f:
        data = json.loads(f)
        #print(type(f))
        #print(f)
        #data = f
        for i in data:
            en = i['en']
            cn = i['cn']
            zidian.append({cn:en})
    print(zidian)

if __name__ == "__main__":
    #get_chinaDayList()
    #themeriver()
    demo()


