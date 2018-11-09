import requests



url = "http://hmcloi.goldensmoke.cn/app/index.php"
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.6.7 NetType/WIFI Language/zh_CN",
           }

parmas_log = {"c":"entry",
              "do":"show",
              "m":"xiaof_toupiao",
              "i":"8",
              "sid":"336",
              "id":"15067",
              "wxref":"mp.weixin.qq.com",
              "from":"timeline",
              "isappinstalled":"0"}

parmas = {"c":"entry",
          "do":"vote",
          "m":"xiaof_toupiao",
          "sid":"336",
          "i":"8",
          "type":"good",
          "id":"15067"}
s = requests.Session()
r_login = s.get(url,headers=headers,params=parmas_log,verify=False)
c=requests.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
c.set('78e6___multiid','8')
s.cookies.update(c)
cookie = s.cookies.get_dict()
print(cookie)



r = requests.get(url,headers=headers,params=parmas,cookies=cookie,verify=False)
print (r.json())