# conding=utf-8

import requests,time

time_os = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

url = "http://127.0.0.1:8000/api/get_event_list"
params = {'eid':'1','name':''}
r = requests.get(url,params=params)
print (r.json())

url1 = "http://127.0.0.1:8000/api/add_event/"
payload = {'eid':1,'name':'红米1','limit':2000,'status':1,'address':'深圳宝体','start_time':time_os}
r = requests.post(url1,data=payload)
print (r.status_code)
print (r.json())